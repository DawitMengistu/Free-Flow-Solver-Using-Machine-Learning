import idx2numpy
import numpy as np
import json

# Initialize lists to hold the puzzles and answers
puzzles = []
answers = []

# Load each .npy file
for i in range(200):  # assuming you have 100 files named 1.npy, 2.npy, ..., 100.npy

    puzzle = np.load("training_ds/g-66-" + str(i) + ".npy")
    answer = np.load("training_ds/a-66-" + str(i) + ".npy")

    puzzles.append(puzzle)
    answers.append(answer)


puzzles_array = np.array(puzzles)
answers_array = np.array(answers)


# print(answers_array[0].flatten())


def scale_to_range(input_array, max_value):
    return np.array([(x / max_value) for x in input_array]).flatten()


def map_values_from_range(input_array, max_value):
    return [round(x * max_value) for x in input_array]


# max_range = np.max(answers_array[0].flatten())
# a = scale_to_range(answers_array[0], max_range)
# b = map_values_from_range(a, max_range)

# print(answers_array[0].flatten())
# print(b)


# Initialize the second layer with 16 neurons
n_inputs = 36  # Assuming input size from MNIST dataset
n_neurons_layer2 = 9
n_neurons_output = 36


lr = 0.1


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class Activation_Sigmoid:
    def forward(self, inputs):
        self.output = sigmoid(inputs)

    def backward(self, dvalues):
        self.dinputs = dvalues * sigmoid_derivative(self.output)


def sigmoid_derivative(x):
    return x * (1 - x)


def calculateErr(result, aim):
    return 0.5 * ((aim - result) ** 2)


# Softmax activation
class Activation_Softmax:
    # Forward pass
    def forward(self, inputs):
        # Get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1,
                                            keepdims=True))
        # Normalize them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1,
                                            keepdims=True)
        self.output = probabilities


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

# layer1_weights.npy
# layer1_biases.npy


class Layer_Dense_Load:
    def __init__(self, n_inputs, n_neurons, pathWeight, pathBiases):
        self.weights = np.load(pathWeight)  # Load weights from file
        self.biases = np.load(pathBiases)    # Load biases from file
        assert self.weights.shape == (
            n_inputs, n_neurons), "Loaded weights shape does not match"
        assert self.biases.shape == (
            1, n_neurons), "Loaded biases shape does not match"

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

 # Save wegiths / biases as Json


# layer1 = Layer_Dense(n_inputs, n_neurons_layer2)
# layer2 = Layer_Dense(n_neurons_layer2, n_neurons_output)

# layer1 = Layer_Dense_Load(
#     n_inputs, n_neurons_layer2, "trained_data/layer1_weights.npy", "trained_data/layer1_biases.npy")
# layer2 = Layer_Dense_Load(
#     n_neurons_layer2, n_neurons_output, "trained_data/layer2_weights.npy", "trained_data/layer2_biases.npy")


# def numpy_to_list(arr):
#     return arr.tolist()


# # Save weights and biases for layer 1
# layer1_data = {
#     'weights': numpy_to_list(layer1.weights),
#     'biases': numpy_to_list(layer1.biases)
# }
# with open('layer1_data.json', 'w') as json_file:
#     json.dump(layer1_data, json_file)

# # Save weights and biases for layer 2
# layer2_data = {
#     'weights': numpy_to_list(layer2.weights),
#     'biases': numpy_to_list(layer2.biases)
# }
# with open('layer2_data.json', 'w') as json_file:
#     json.dump(layer2_data, json_file)

layer1 = Layer_Dense(n_inputs, n_neurons_layer2)
layer2 = Layer_Dense(n_neurons_layer2, n_neurons_output)


# layer1 = Layer_Dense_Load(
#     n_inputs, n_neurons_layer2, "trained_data/layer1_weights.npy", "trained_data/layer1_biases.npy")
# layer2 = Layer_Dense_Load(
#     n_neurons_layer2, n_neurons_output, "trained_data/layer2_weights.npy", "trained_data/layer2_biases.npy")

for z in range(2000):
    perm = np.random.permutation(len(puzzles_array))
    puzzles_array = puzzles_array[perm]
    answers_array = answers_array[perm]

    batch_size = 100
    num_batches = len(puzzles_array)
    num_epochs = 100

    for epoch in range(num_epochs):
        total_error = 0
        for batch in range(num_batches):
            batch_start = batch * batch_size
            batch_end = batch_start + batch_size

            dW1_sum = np.zeros_like(layer1.weights)
            dB1_sum = np.zeros_like(layer1.biases)
            dW2_sum = np.zeros_like(layer2.weights)
            dB2_sum = np.zeros_like(layer2.biases)

            for i in range(batch_start, batch_end):
                if (i < 200):
                    layer1.forward(puzzles_array[i].flatten())
                    activation1 = Activation_Sigmoid()
                    activation1.forward(layer1.output)

                    layer2.forward(activation1.output)
                    activation2 = Activation_Sigmoid()
                    activation2.forward(layer2.output)

                    outputLayer = activation2.output

                    max_range = np.max(answers_array[i].flatten())
                    target = scale_to_range(
                        answers_array[i].flatten(), max_range)
                    error = calculateErr(outputLayer, target)
                    total_error += np.sum(error)

                    dOut = -(target - outputLayer)
                    activation2.backward(dOut)
                    dNet2 = activation2.dinputs

                    dW2_sum += np.outer(activation1.output, dNet2)
                    dB2_sum += dNet2

                    dA1 = np.dot(dNet2, layer2.weights.T)
                    activation1.backward(dA1)
                    dNet1 = activation1.dinputs

                    dW1_sum += np.outer(puzzles_array[i].flatten(), dNet1)
                    dB1_sum += dNet1

            layer2.weights -= lr * (dW2_sum / batch_size)
            layer2.biases -= lr * (dB2_sum / batch_size)
            layer1.weights -= lr * (dW1_sum / batch_size)
            layer1.biases -= lr * (dB1_sum / batch_size)
        if (epoch % 10 == 0):
            print(
                f"Epoch {epoch + 1}, Total Error: {total_error / num_batches}")
            # Save weights and biases for layer 1
            np.save('trained_data/layer1_weights.npy', layer1.weights)
            np.save('trained_data/layer1_biases.npy', layer1.biases)

            # Save weights and biases for layer 2
            np.save('trained_data/layer2_weights.npy', layer2.weights)
            np.save('trained_data/layer2_biases.npy', layer2.biases)

for i in range(0):
    epochs = 15
    errors = []
    batch_size = 100
    batch_accumulation = 100

    layer1 = Layer_Dense(n_inputs, n_neurons_layer2)
    layer2 = Layer_Dense(n_neurons_layer2, n_neurons_output)

    # layer1 = Layer_Dense_Load(
    #     n_inputs, n_neurons_layer2, "layer1_weights.npy", "layer1_biases.npy")
    # layer2 = Layer_Dense_Load(
    #     n_neurons_layer2, n_neurons_output, "layer2_weights.npy", "layer2_biases.npy")

    for epoch in range(epochs):
        epoch_error = 0
        accumulated_dW1 = 0
        accumulated_dB1 = 0
        accumulated_dW2 = 0
        accumulated_dB2 = 0

        for batch_idx in range(len(images) // batch_size):
            start_idx = batch_idx * batch_size
            end_idx = start_idx + batch_size

            # Iterate over images in the batch
            for image_index in range(start_idx, end_idx):
                image = images[image_index]
                flattened_image = image.reshape(-1)

                # Forward pass
                layer1.forward(flattened_image)
                activation1 = Activation_Sigmoid()
                activation1.forward(layer1.output)

                layer2.forward(activation1.output)
                activation2 = Activation_Sigmoid()
                activation2.forward(layer2.output)

                outputLayer = activation2.output

                # Calculate output error
                target = np.eye(10)[labels[image_index]]
                error = calculateErr(outputLayer, target)
                total_error = np.sum(error)
                epoch_error += total_error

                # Backward pass for output layer
                dOut = -(target - outputLayer)
                activation2.backward(dOut)
                dNet2 = activation2.dinputs

                # Gradients for weights and biases between hidden layer and output layer
                dW2 = np.outer(activation1.output, dNet2)
                dB2 = dNet2

                # Calculate error term for hidden layer
                dA1 = np.dot(dNet2, layer2.weights.T)
                activation1.backward(dA1)
                dNet1 = activation1.dinputs

                # Gradients for weights and biases between input layer and hidden layer
                dW1 = np.outer(flattened_image, dNet1)
                dB1 = dNet1

                # Accumulate gradients
                accumulated_dW2 += dW2
                accumulated_dB2 += dB2
                accumulated_dW1 += dW1
                accumulated_dB1 += dB1

            # Update weights and biases after accumulating gradients over `batch_accumulation` batches
            if (batch_idx + 1) % batch_accumulation == 0:
                layer2.weights -= lr * (accumulated_dW2 / batch_accumulation)
                layer2.biases -= lr * (accumulated_dB2 / batch_accumulation)
                layer1.weights -= lr * (accumulated_dW1 / batch_accumulation)
                layer1.biases -= lr * (accumulated_dB1 / batch_accumulation)

                # Reset accumulated gradients
                accumulated_dW2 = 0
                accumulated_dB2 = 0
                accumulated_dW1 = 0
                accumulated_dB1 = 0

        # Calculate average epoch error
        average_epoch_error = epoch_error / len(images)
        errors.append(average_epoch_error)

        # Print progress
        if epoch % 10 == 0:
            print(f'Epoch {epoch}, Average Error: {average_epoch_error}')

    # Calculate percentage improvement
    # initial_error = errors[0]
    # final_error = errors[-1]
    # improvement = ((initial_error - final_error) / initial_error) * 100
    # print(f'Initial Error: {initial_error}')
    # print(f'Final Error: {final_error}')
    # print(f'Improvement: {improvement}%')

    # Save weights and biases for layer 1
    np.save('layer1_weights.npy', layer1.weights)
    np.save('layer1_biases.npy', layer1.biases)

    # Save weights and biases for layer 2
    np.save('layer2_weights.npy', layer2.weights)
    np.save('layer2_biases.npy', layer2.biases)


# print(outputLayer)
