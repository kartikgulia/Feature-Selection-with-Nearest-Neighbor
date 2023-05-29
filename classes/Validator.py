from typing import List
import sys
import math
#from Classifier import 

def leave_one_out_cross_validation(self, test_instance) -> float:
	number_correctly_classfied = 0
	for i in range(1, len(test_instance)+1):
		object_to_classify = self.dataset[test_instance-1][1:]
		label_of_object_to_classify = self.dataset[test_instance-1][0]
	
		numTrainingRows : int = len(self.idToClassLabelAndDataMap)

		nearestNeighborDistance = float('inf')
		nearestNeighborClass = float('inf')

		for key, value in self.idToClassLabelAndDataMap.items():
			classLabelForEachInstance = value[0]
			trainingDataForEachInstance = value[1]
			distance = 0
			for i in range(len(trainingDataForEachInstance)):
				distance += math.pow((object_to_classify[0] - trainingDataForEachInstance[i]),2)
			distance = math.sqrt(distance)

			if distance < nearestNeighborDistance:
				nearestNeighborDistance = distance
				nearestNeighborClass = classLabelForEachInstance

		if label_of_object_to_classify == nearestNeighborClass:
			number_correctly_classfied += 1
	return number_correctly_classfied/(len(test_instance)+1)