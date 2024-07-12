const grid = document.querySelector(".grid-con")
let game = [[0, 0, 1, 2, 3, 4],
[1, 2, 0, 0, 0, 0],
[3, 0, 5, 6, 0, 0],
[0, 0, 6, 0, 0, 0],
[0, 0, 5, 0, 0, 0],
[0, 0, 0, 0, 4, 0]]


let colors = ["red", "yellow", "green", "blue", "purple", "orange", "pink"]


for (let i = 0; i < 36; i++) {
    let row = Math.floor(i / 6);
    let col = i % 6;

    grid.innerHTML += `
    <div class="single-grid-puzzle">
        ${game[row][col] !== 0 ? `<div class="point ${colors[game[row][col]]}"></div>` : ''}
    </div>`;

}


const singleGrid = document.querySelectorAll(".single-grid-puzzle")
const lineName = ["up-line", "down-line", "left-line", "right-line"]


for (let i = 0; i < 4; i++) {
    for (let g = 0; g < 36; g++) {
        singleGrid[g].innerHTML += `<div class="inner-line ${lineName[i]}"></div>`
    }
}

console.log("Hello World")
let prevX = null;
let prevY = null;

for (let g = 0; g < 36; g++) {
    singleGrid[g].addEventListener("mousemove", (event) => {
        console.log("Here")
        const direction = getMouseDirection(event);
        if (direction) {
            console.log("Mouse is moving:", direction);
        }
    })
}



function getMouseDirection(event) {
    const currentX = event.clientX;
    const currentY = event.clientY;
    let direction = null;

    if (prevX !== null && prevY !== null) {
        const deltaX = currentX - prevX;
        const deltaY = currentY - prevY;

        if (Math.abs(deltaX) > Math.abs(deltaY)) {
            // Horizontal movement
            direction = deltaX > 0 ? "right" : "left";
        } else {
            // Vertical movement
            direction = deltaY > 0 ? "down" : "up";
        }
    }

    prevX = currentX;
    prevY = currentY;

    return direction;
}


