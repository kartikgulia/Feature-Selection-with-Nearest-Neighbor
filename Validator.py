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
		

		

	def calculate_accuracy(self):
		numberOfRows = len(self.fullDataset)
		print(numberOfRows)



v = Validator([10] , "large-test-dataset-1.txt")
v.calculate_accuracy()