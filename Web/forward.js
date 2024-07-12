import fs from 'fs'
import * as math from 'mathjs';

class LayerDense {
    constructor(weights, biases) {
        this.weights = weights;
        this.biases = biases;
    }

    forward(inputs) {
        this.output = math.add(math.multiply(inputs, this.weights), this.biases);
    }
}

function sigmoid(x) {
    return math.dotDivide(1, math.add(1, math.exp(math.unaryMinus(x))));
}

// Apply the sigmoid function element-wise to a matrix
function sigmoidMatrix(matrix) {
    return math.map(matrix, x => sigmoid(x));
}



// Load the data from the JSON file
const data1 = fs.readFileSync('layer1_data.json', 'utf8');
const data2 = fs.readFileSync('layer2_data.json', 'utf8');
const testFile = fs.readFileSync('test_ds/test_data.json', 'utf8');
const trainingFile = fs.readFileSync('trained_ds/trained_ds.json', 'utf8');
const test_data = JSON.parse(testFile)
const trainingData = JSON.parse(trainingFile)

const LayerOneData = JSON.parse(data1);
const LayerTwo = JSON.parse(data2);

// Initialize the layer with the loaded data
const layer1 = new LayerDense(LayerOneData.weights, LayerOneData.biases);
const layer2 = new LayerDense(LayerTwo.weights, LayerTwo.biases);


function mapValuesFromRange(inputArray, maxValue) {
    return inputArray.map(x => Math.round(x * maxValue));
}


export function getData() {
    let random_index = Math.floor(Math.random() * 70)
    // let testArr = test_data.puzzle[random_index]
    // let ansArr = test_data.answer[random_index]
    let testArr = trainingData.puzzle[random_index]
    let ansArr = trainingData.answer[random_index]



    // Perform forward pass through the first layer
    layer1.forward(math.flatten(testArr));
    const activation1 = sigmoidMatrix(layer1.output);


    // Perform forward pass through the second layer
    layer2.forward(activation1);
    const outputLayer = sigmoidMatrix(layer2.output);
    // console.log(outputLayer[0])

    let outputArr = mapValuesFromRange(outputLayer[0], Math.max(...math.flatten(ansArr)))
    return { answer: math.reshape(outputArr, [6, 6]), game: testArr, pridiction: ansArr, index: random_index }
    // console.log('\n', ansArr)
    // // return mapValuesFromRange(outputLayer[0]);
}



console.log(getData())
