# 1.1
# How does data enable machine learning?
# example: images of animals, properties of a flower, properties of a house
input = [1, 2, 3, 4, 5]
# example: labels of animal names, labels of flower names, house price
output = [2, 4, 6, 8, 10]

# What is rule based programming?
def smart_function(input):
    return input * 2

smart_function(input)

# Three ingredients of ML - data, model, feedback loop
# data
input, output
# model
# e.g. linear model = input * constant

# feedback loop
# error = machine_learned_output - output
input, output = (1, 2)
model, prediction[1] = 3
error = 3 - 2 = 1

# What actually is a ML model? a simplification of real life

# 1.2
# Machine learning is all about predicting things
# Regression is the task of predicting numbers
input = [0, 1, 2, 3, 4]
output = [0, 2, 4, 6, 8]

# Classification is the task of predicting labels
input = [0, 1, 2, 3, 4]
labels = ["doesn't exist", "cane", "person", "tricycle", "car"]

# Other predictive tasks

# 1.4

# Supervised Learning
input = [1, 2, 3, 4, 5]
output = [2, 4, 6, 8, 10]

# Unsupervised Learning
input = [1, 2, 3, 6, 7, 8]

# Reinforcement Learning
state = (internal state, environment)
action = prediction
reward 