from SimpleFNN import SimpleFNN;

# XOR input and output
data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

# Create model with 2 inputs, 2 hidden neurons, 1 output
model = SimpleFNN(input_size=2, hidden_size=2, output_size=1)

# Train the model
for epoch in range(5000):
    total_error = 0
    for inputs, target in data:
        error = model.train(inputs, target, learning_rate=0.5)
        total_error += error
    if epoch % 500 == 0:
        print(f"Epoch {epoch}, Error: {total_error:.4f}")

# Test the model
print("\n--- Testing XOR ---")
for inputs, _ in data:
    prediction = model.forward(inputs)
    print(f"Input: {inputs}, Output: {round(prediction, 3)}")
