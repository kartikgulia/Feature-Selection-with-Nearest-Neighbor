from typing import List
import sys
import math
from Classifier import Classifier
from datasetActions import read_dataset
from datasetActions import filter_dataset
class Validator:
    
	#  classifier : Classifier,

	def __init__(self, featureSubset : List[int] , textfileName : str):

		self.featureSubset : set = featureSubset
		
		self.fullDataset : List[List[float]] = read_dataset(textfileName)

		datasetWithSubsetOfFeatures = filter_dataset(self.fullDataset,featureSubset)

		self.classifier = Classifier(datasetWithSubsetOfFeatures)
		

	def calculate_accuracy(self) -> float:

		numberOfRows = len(self.fullDataset)
		
		numberOfCorrectPredictions = 0

		listOfTrainingIds = list(range(numberOfRows))
		# iterate through each ID and exclude it from training
		for i in range(0,numberOfRows):
			
			correctLabel = self.fullDataset[i][0]

			# remove the test ID from list
			listOfTrainingIds.pop(i)
			
			# train model without the test ID
			self.classifier.train(listOfTrainingIds)

			# test the removed ID
			predictedLabel = self.classifier.test(i)

			if(predictedLabel == correctLabel):
				numberOfCorrectPredictions += 1

			# put back the removed ID
			listOfTrainingIds.insert(i,i)
			
			# clear dictionary for next use
			self.classifier.clearDictionary()

		return numberOfCorrectPredictions / numberOfRows
	

# v = Validator([3,5,7] , "small-test-dataset.txt")
# print(v.calculate_accuracy())

# v = Validator([1,15,27] , "large-test-dataset-1.txt")
# print(v.calculate_accuracy())