import math
import random

# Activation function and its derivative
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network class
class SimpleFNN:
    def __init__(self, input_size, hidden_size, output_size):
        # Random weights for input -> hidden
        self.weights_input_hidden = [[random.uniform(-1, 1) for _ in range(hidden_size)] for _ in range(input_size)]
        self.bias_hidden = [random.uniform(-1, 1) for _ in range(hidden_size)]

        # Random weights for hidden -> output
        self.weights_hidden_output = [random.uniform(-1, 1) for _ in range(hidden_size)]
        self.bias_output = random.uniform(-1, 1)

    def forward(self, inputs):
        # Calculate hidden layer activations
        self.hidden_input = []
        self.hidden_output = []
        for j in range(len(self.bias_hidden)):
            sum_h = sum(inputs[i] * self.weights_input_hidden[i][j] for i in range(len(inputs))) + self.bias_hidden[j]
            self.hidden_input.append(sum_h)
            self.hidden_output.append(sigmoid(sum_h))

        # Calculate output layer activation
        sum_o = sum(self.hidden_output[j] * self.weights_hidden_output[j] for j in range(len(self.hidden_output))) + self.bias_output
        self.output = sigmoid(sum_o)
        return self.output

    def train(self, inputs, target, learning_rate=0.1):
        output = self.forward(inputs)

        # Compute error at output
        output_error = target - output
        output_delta = output_error * sigmoid_derivative(output)

        # Compute error at hidden layer
        hidden_deltas = []
        for j in range(len(self.hidden_output)):
            error = output_delta * self.weights_hidden_output[j]
            delta = error * sigmoid_derivative(self.hidden_output[j])
            hidden_deltas.append(delta)

        # Update weights hidden -> output
        for j in range(len(self.weights_hidden_output)):
            self.weights_hidden_output[j] += learning_rate * output_delta * self.hidden_output[j]
        self.bias_output += learning_rate * output_delta

        # Update weights input -> hidden
        for i in range(len(inputs)):
            for j in range(len(self.weights_input_hidden[0])):
                self.weights_input_hidden[i][j] += learning_rate * hidden_deltas[j] * inputs[i]
        for j in range(len(self.bias_hidden)):
            self.bias_hidden[j] += learning_rate * hidden_deltas[j]

        return output_error ** 2  # Return squared error
