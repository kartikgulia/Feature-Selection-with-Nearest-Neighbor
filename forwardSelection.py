from randAccuracy import accuracy
from itertools import combinations
import copy
# def FS(featureNum):
# 	maxAcc = accuracy()
# 	maxFeature = 0
# 	bestFeature = 0
# 	bestAcc = 0
	
# 	print(f"Using no features and “random” evaluation, I get an accuracy of: {maxAcc} ")

# 	for i in range(1,featureNum):
# 		if (i==1):
# 			print("Beginning Search")
# 		else:
# 			print(f"Feature set {bestFeature} was best, accuray is: {bestAcc}%")
# 		for j in range(1,featureNum):
# 			temp = accuracy()
# 			print(f"Using feature(s) {j} accuracy is {temp}%")
# 			if (temp > bestAcc):
# 				bestFeature = j
# 				bestAcc = temp
# 			if (temp > maxAcc):
# 				maxFeature = j
# 				maxAcc = temp

# def FS(featureNum):
# 	bestSet = set()
# 	#bestAcc = 0.0

# 	bestAcc = accuracy()
# 	print(f"Using no features and “random” evaluation, I get an accuracy of: {bestAcc}%")
# 	print("Beginning Search")

# 	for i in range(1, featureNum+1):
# 		currSet = bestSet.copy()
# 		expand = None
# 		bestSetAcc = bestAcc

# 		for j in range(1, featureNum+1):
# 			if j not in currSet:
# 				currSet.add(j)
# 				temp = accuracy()
# 				print(f"Using feature(s) {currSet} accuracy is {temp}%")
# 				if (temp > bestSetAcc):
# 					bestSetAcc = temp
# 					expand = j
# 				currSet.remove(j)
# 		if (expand == None):
# 			break
# 		currSet.add(expand)
# 		if (bestSetAcc > bestAcc):
# 			bestAcc = bestSetAcc
# 			bestSet = currSet.copy()
# 			print(f"Feature set {currSet} was best, accuracy is {bestAcc}%")
# 		else:
# 			print(f"Warning, accuracy decreased!")
# 		# if (len(bestSet) == featureNum):
# 		# 	break
# 	print(f"Finished Search. Best Feature subset is {bestSet}, which has an accurary of {bestAcc}%")


# def FS(featureNum):
# 	bestSet = set()
# 	#bestAcc = 0.0
# 	cycleSet = set()
	
# 	bestAcc = accuracy()
	
# 	print(f"Using no features and “random” evaluation, I get an accuracy of: {bestAcc}%")
# 	print("Beginning Search")

# 	for i in range(1, featureNum+1):
# 		totalcombinations = combinations(range(1, featureNum+1), i)

# 		for j in totalcombinations:
# 			#print(f"\nj:{j}, bestSet: {bestSet}\n")
# 			if (len(j) > 1 and bestSet.issubset(set(j))):
				
# 				temp = accuracy()
# 				print(f"Using feature(s) {j} accuracy is {temp}%")
				

# 				if (temp > bestAcc):
# 						bestAcc = temp
# 						bestSet = set(j)
# 						print(f"Feature set {bestSet} was best, accuracy is {bestAcc}%")
# 				else:
# 					print(f"Warning, accuracy decreased!")
# 			elif (len(j) == 1):
# 				temp = accuracy()
# 				print(f"Using feature(s) {j} accuracy is {temp}%")
# 				if (temp > bestAcc):
# 						bestAcc = temp
# 						bestSet = set(j)
# 						print(f"Feature set {bestSet} was best, accuracy is {bestAcc}%")
# 				else:
# 					print(f"Warning, accuracy decreased!")
# 		# if (bestSet.issubset(set(j))):
# 		# 	break
# 	print(f"Finished Search. Best Feature subset is {bestSet}, which has an accurary of {bestAcc}%")

def FS(featureNum):
	bestSet = []
	bestAcc = 0.0
	currSet = []
	print("Beginning Search.")
	for i in range(featureNum):
		currAcc = 0.0
		bestChecker = -1
		worseChecker = -1
		for j in range(1, featureNum + 1):
			if j not in currSet:
				node = copy.deepcopy(currSet)
				node.append(j)
				temp = accuracy()
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
		else:
			currSet.append(worseChecker)
			print(f"(Warning, Accuracy has decreased!!)")
			print(f"Feature set {sorted(currSet)} was best, accuracy is {currAcc}%")

	print(f"Finished Search! The best feature subset is {bestSet} which has an accuracy of {bestAcc}%")