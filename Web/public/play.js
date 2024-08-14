const grid = document.querySelector(".grid-con")
let game = [[0, 0, 1, 2, 3, 4],
[1, 2, 0, 0, 0, 0],
[3, 0, 5, 6, 0, 0],
[0, 0, 6, 0, 0, 0],
[0, 0, 5, 0, 0, 0],
[0, 0, 0, 0, 4, 0]]

let gameGrid = game;


// let colors = ["red", "yellow", "green", "blue", "purple", "orange", "pink", "white"]




for (let i = 0; i < 36; i++) {
    let row = Math.floor(i / 6);
    let col = i % 6;

    grid.innerHTML += `
<div class="single-grid-puzzle">
    ${game[row][col] !== 0 ? `<div class="point ${colors[game[row][col]]}"></div>` : ''}
</div>`;
}


function updateGrid() {
    for (let i = 0; i < 36; i++) {
        let row = Math.floor(i / 6);
        let col = i % 6;

        singleGrid
    }
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


let currentLoc = [-15, -15];

let row = 0
let col = 0
let mousedown = false;


for (let g = 0; g < 36; g++) {



    singleGrid[g].addEventListener("mousemove", () => {
        row = Math.floor(g / 6);
        col = g % 6;
        // console.log(currentLoc[0], row, currentLoc[0] + 1, row == currentLoc[0] + 1, " ", currentLoc[1], col, currentLoc[1] + 1, col == currentLoc[1] + 1)
        if (mousedown && (currentLoc[0] == -15 || isValidStep(currentLoc[0], currentLoc[1], row, col))) {
            if (mousedown && (currentLoc[0] != row || currentLoc[1] != col) && gameGrid[row][col] != -1) {

                gameGrid[row][col] = -1
                singleGrid[g].style.backgroundColor = "white"

                try {
                    gameGrid[currentLoc[0]][currentLoc[1]] = -1
                    singleGrid[currentLoc[0] * 6 + currentLoc[1]].style.backgroundColor = "white"
                } catch (e) {

                }

                currentLoc[0] = row
                currentLoc[1] = col
            }
            else if ((currentLoc[0] != row || currentLoc[1] != col) && gameGrid[row][col] == -1) {
                console.log("There")
                gameGrid[currentLoc[0]][currentLoc[1]] = 0
                singleGrid[currentLoc[0] * 6 + currentLoc[1]].style.backgroundColor = "black"

                gameGrid[row][col] = 0
                singleGrid[g].style.backgroundColor = "black"
                currentLoc[0] = row
                currentLoc[1] = col
            }
        }

    });
}


// Event listener for mouse down
document.addEventListener('mousedown', function () {
    mousedown = true;
});

// Event listener for mouse up
document.addEventListener('mouseup', function () {
    mousedown = false;
    currentLoc = [-15, -15];
});

// Event listener for mouse leaving the window
document.addEventListener('mouseleave', function () {
    mousedown = false;
    console.log('Mouse left the window');
});



function isValidStep(px, py, x, y) {
    // Calculate the difference in x and y coordinates
    var dx = Math.abs(x - px);
    var dy = Math.abs(y - py);

    // Check if the step is valid (one step in one direction only)
    if ((dx === 1 && dy === 0) || (dx === 0 && dy === 1)) {
        return true;
    }

    // If it's not a valid step
    return false;
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


