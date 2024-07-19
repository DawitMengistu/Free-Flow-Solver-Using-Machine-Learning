let colors = ["#FF0000", " #008000", " #EEEE00", " #0000FF", " #800080", " #FF7F00", " #FF00FF"]

const canvas = document.querySelector(".canvas");
const canvas2 = document.querySelector(".canvas2");
const canvas3 = document.querySelector(".canvas3");


for (let i = 0; i < 36; i++) {
    canvas.innerHTML += `  <div class="single-grid-puzzle"></div>`
}

for (let i = 0; i < 36; i++) {
    canvas2.innerHTML += `  <div class="single-grid-answer"></div>`
}
for (let i = 0; i < 36; i++) {
    canvas3.innerHTML += `  <div class="single-grid-pridiction"></div>`
}

const singleGridPuzzle = document.querySelectorAll(".single-grid-puzzle")
const singleGridAnswer = document.querySelectorAll(".single-grid-answer")
const singleGridPridiction = document.querySelectorAll(".single-grid-pridiction")



const load = document.querySelector(".load-btn");


load.addEventListener("click", async () => {
    let data = await getData();
    console.log(data, typeof (data))
    let game = data.game;
    let ans = data.answer;
    let pridiction = data.pridiction;


    for (let g = 0; g < 6; g++)
        for (let i = 0; i < 6; i++) {
            const index = g * 6 + i;
            singleGridPuzzle[index].innerHTML = "";
            if (game[g][i] != 0) {
                singleGridPuzzle[index].innerHTML += `<div class="point" style="background-color: ${colors[game[g][i]]};"></div>`;
            }

            singleGridAnswer[index].innerHTML = "";
            singleGridAnswer[index].innerHTML += `<div class="point" style="background-color: ${colors[pridiction[g][i] + 1]};"></div>`;

            singleGridPridiction[index].innerHTML = "";
            singleGridPridiction[index].innerHTML += `<div class="point" style="background-color: ${colors[ans[g][i] + 1]};"></div>`;

        }

})





async function getData() {
    return fetch("http://localhost:3000/getrandom", {
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(response => response.json())
        .then(data => {
            return data
        })
        .catch(error => console.error(error));
}

