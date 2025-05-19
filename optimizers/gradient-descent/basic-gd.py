X = [1,2,3,4,5]
Y=[2,4,6,8,10]

print("X:", X)
print("Y:", Y)
# initializing the parameters
W = 0.0
b = 0.0
# learning rate
lr = 0.01
# number of epochs
epochs = 1000
# number of samples
m = len(X)
# gradient descent
for epoch in range(epochs):
    y_pred = [W * x + b for x in X]
    # calculate the gradients
    dW = (-2/m) * sum([(Y[i] - y_pred[i]) * X[i] for i in range(m)])
    db = (-2/m) * sum([Y[i] - y_pred[i] for i in range(m)])
    # update the parameters
    W = W - lr * dW
    b = b - lr * db
    # print the loss
    if epoch % 100 == 0:
        loss = (1/m) * sum([(Y[i] - y_pred[i]) ** 2 for i in range(m)])
        print(f'Epoch {epoch}, Loss: {loss}, W: {W}, b: {b}')
# final parameters
print(f'\nFinal parameters: W: {W}, b: {b}')