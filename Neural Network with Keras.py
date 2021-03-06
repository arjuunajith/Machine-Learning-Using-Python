from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# Loading the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')

# Splitting into input and output variables
X = dataset[:, 0:8]
y = dataset[:, 8]

# Defining the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fitting the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)

# Evaluating the keras model
# _, accuracy = model.evaluate(X, y)
# print('Accuracy: %.2f' % (accuracy*100))

# Making class predictions with the model
predictions = model.predict_classes(X)

# Summarize the first 5 cases
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
