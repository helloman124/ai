import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, max_iterations=1000):
        self.weights = np.random.rand(input_size)
        self.threshold = np.random.rand()
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations

    def predict(self, inputs):
        activation = np.dot(inputs, self.weights) - self.threshold
        return 1 if activation > 0 else 0

    def train(self, training_data, labels):
        for iteration in range(self.max_iterations):
            errors = 0
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                if error != 0:
                    self.weights += self.learning_rate * error * inputs
                    self.threshold -= self.learning_rate * error
                    errors += 1
            if errors == 0:
                print(f"Converged in {iteration + 1} iterations")
                break
        else:
            print("Did not converge within the maximum number of iterations")

# Example usage:
if __name__ == "__main__":
    # Example training data (2D)
    training_data = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    # Example labels (AND gate)
    labels = np.array([0, 0, 0, 1])

    # Initialize and train the perceptron
    perceptron = Perceptron(input_size=2)
    perceptron.train(training_data, labels)

    # Test the trained perceptron
    test_data = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    print("\nTest results:")
    for inputs in test_data:
        prediction = perceptron.predict(inputs)
        print(f"Inputs: {inputs}, Prediction: {prediction}")
