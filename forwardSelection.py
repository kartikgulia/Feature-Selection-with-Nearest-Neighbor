from randAccuracy import accuracy
from itertools import combinations
import copy
from Validator import Validator

from plotTrace import plotTraceGraph

def FS(featureNum, textfileName):
	bestSet = []
	bestAcc = 0.0
	currSet = []

	bestSetLength2 = []

	print("Beginning Search.")
	for i in range(featureNum):
		currAcc = 0.0
		bestChecker = -1
		worseChecker = -1
		for j in range(1, featureNum + 1):
			if j not in currSet:
				node = copy.deepcopy(currSet)
				node.append(j)
				v : Validator = Validator(node,textfileName)
				temp = v.calculate_accuracy()
				print(f"Using feature(s) {sorted(node)} accuracy is {temp}%")
				if temp > currAcc:
					currAcc = temp
					worseChecker = j
				if temp > bestAcc:
					bestAcc = temp
					bestChecker = j
		if bestChecker >= 0:
			currSet.append(bestChecker)
			bestSet.append(bestChecker)
			print(f"Feature set {sorted(currSet)} was best, accuracy is {bestAcc}%")

			if(len(currSet) == 2):
				bestSetLength2 = currSet
		else:
			currSet.append(worseChecker)
			print(f"(Warning, Accuracy has decreased!!)")
			print(f"Feature set {sorted(currSet)} was best, accuracy is {currAcc}%")

	print(f"Finished Search! The best feature subset is {bestSet} which has an accuracy of {bestAcc}%")

	plotTraceGraph(bestSetLength2, textfileName)