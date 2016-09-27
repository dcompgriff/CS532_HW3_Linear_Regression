import numpy as np
import scipy.linalg as linalg



def question4():
	pass

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

	print('Part c ans: ')
	A2 = np.array([[25, 15, 10, 0, 1],
	               [20, 12, 8, 1, 2],
	               [40, 30, 10, 1, 6],
	               [30, 15, 15, 0, 3],
	               [35, 20, 15, 2, 4]])
	A3 = np.array([[25, 15, 10, 0, 1],
	               [20, 12, 8, 1, 2],
	               [40, 30, 10, 1, 6],
	               [30, 15, 15, 0, 3],
	               [35, 20, 15, 2, 4]])
	b2 = np.array([[104],
	               [97],
	               [193],
	               [132],
	               [174]])
	try:
		print(linalg.solve(A2, b2))
	except:
		print('Singular matrix!')

	print('Part c true calories per gram: ')
	for rowInd in range(0, A2.shape[0]):
		if np.dot(A2[rowInd, 0:3], b2[0:3]) == trueX[rowInd]:
			print('Matching Row: ')
			print(A2[rowInd, :])


if __name__ == '__main__':
	question4()
	question5()








