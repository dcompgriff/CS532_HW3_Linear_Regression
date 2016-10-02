import numpy as np
import pandas as pd
import scipy.linalg as linalg
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def question4():
	degrees = [1, 2, 3]#[1, 2, 3]
	plotColors = ['blue', 'green', 'red']
	plotHandles = []

	data = pd.read_csv('./data.csv', header=None, names=['x', 'y'])

	plt.scatter(list(data.x), list(data.y))

	#Expand x into the polynomial data matrix.
	for d in degrees:
		A = np.ones((len(data.x), d + 1))
		for rowInd in range(0, len(data.x)):
			for col in range(1, len(A[0])):
				A[rowInd, col] = data.iloc[rowInd]['x']**col

		#Find coeffecients.
		coeff = linalg.solve(np.dot(A.T,A), np.dot(A.T, (data.y.values).reshape((len(data.y), 1))))
		regressionFunctOutput = []
		for i in np.linspace(min(list(data.x)), max(list(data.x))):
			dataVect = np.ones((1, d+1))
			for col in range(1, len(A[0])):
				dataVect[0, col] = i**col
			regressionFunctOutput.append((i, (np.dot(dataVect, coeff)[0, 0])))
		plt.plot(list(map(lambda item: item[0], regressionFunctOutput)), list(map(lambda item: item[1], regressionFunctOutput)), color=plotColors[d-1])
		plotHandles.append(mpatches.Patch(color=plotColors[d-1], label='Degree ' + str(d)))
		print(regressionFunctOutput)
	plt.title('Polynomial Regression Curves')
	plt.xlabel('X data')
	plt.ylabel('Y data')
	plt.legend(handles=plotHandles, loc=2)
	plt.show()

def question5():
	A = np.array([[25, 0, 1],
	                [20, 1, 2],
	                [40, 1, 6]])

	b = np.array([[110],
	                [110],
	                [210]])
	trueX = np.array([[4],
	                  [9],
	                  [4]])

	print('Part a ans: ')
	print(linalg.solve(A, b))

	print('Part b ans: ')
	print((1/9.0)*((-4*np.array([A[:, 2]]).T) + (-4*np.array([A[:, 0]]).T) + b))


if __name__ == '__main__':
	question4()
	question5()








