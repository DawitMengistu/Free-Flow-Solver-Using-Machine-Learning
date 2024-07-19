const lineCon = document.querySelector(".bg-line-con")
let verArr = []
let horArr = []
let speed = []
let lineLen = 22;

for (let i = 0; i < lineLen; i++) {
    lineCon.innerHTML += `<div class="single-line ${i % 2 == 0 ? "ver" : "hor"}"></div>`
}

const lines = document.querySelectorAll(".single-line")
let colorArr = ["red", "yellow", "green", "blue", "purple", "orange", "pink", "white"]

initializeSize()
updatePos();

function initializeSize() {
    for (let i = 0; i < lineLen; i++) {
        ele = lines[i];

        if (ele.classList.contains("hor")) {

            ele.classList.add(colorArr[getRandom(colorArr.length)])
            ele.style.width = getRandomLen(window.innerWidth / 2, window.innerWidth / 1.3) + "px";
            ele.style.height = "23px";

            horArr.push([0, getRandom(window.innerHeight)])
        } else {
            ele.classList.add(colorArr[getRandom(colorArr.length)])
            ele.style.width = "23px";
            ele.style.height = getRandomLen(window.innerHeight / 2, window.innerHeight / 1.3) + "px";

            verArr.push([getRandom(window.innerWidth), 0])
        }
    }

    console.log(verArr)
    console.log(horArr)
}
for (let i = 0; i < lineLen; i++) {
    speed.push(getRandomLen(0.5, 3))
}

setInterval(() => {
    let indexV = 0;
    let indexH = 0;
    for (let i = 0; i < lineLen; i++) {
        ele = lines[i];
        if (ele.classList.contains("hor")) {
            if (horArr[indexH][0] >= (window.innerWidth + parseInt(ele.style.width, 10))) {
                console.log("I'm here")
                horArr[indexH][0] = - parseInt(ele.style.width, 10);
            }
            horArr[indexH][0] += speed[i];
            indexH += 1;
        } else {
            if (verArr[indexV][1] >= (window.innerHeight + parseInt(ele.style.height, 10))) {
                console.log("I'm here")
                verArr[indexV][1] = - parseInt(ele.style.height, 10);
            }
            verArr[indexV][1] += speed[i];
            indexV += 1;
        }
    }
    updatePos();
}, 7);




function updatePos() {
    let indexV = 0;
    let indexH = 0;
    for (let i = 0; i < lineLen; i++) {
        ele = lines[i];
        if (ele.classList.contains("hor")) {
            ele.style.top = horArr[indexH][1] + "px"
            ele.style.left = `${horArr[indexH][0] - parseInt(ele.style.width, 10)}px`
            indexH += 1;
        }
        else {
            ele.style.top = `${verArr[indexV][1] - parseInt(ele.style.height, 10)}px`
            ele.style.right = verArr[indexV][0] + "px";
            indexV += 1;
        }
    }
}




function getRandom(n) {
    return Math.floor(Math.random() * n)
}
function getRandomLen(n, m) {
    return Math.floor(Math.random() * (m - n + 1)) + n;
}
