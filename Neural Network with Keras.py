from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# Loading the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')

# Splitting into input (X) and output (y) variables
X = dataset[:, 0:8]
y = dataset[:, 8]
