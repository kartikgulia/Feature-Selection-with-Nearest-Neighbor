from typing import List
import sys
import math



# This class does two things:
    # 1) Trains the Classifier with the input data from the text files 
        # Stores the information from the text file in a map ---> ID : rowData

    # 2) Tests the Classifier --> returns predicted class label
        # Takes a row number (test_instance) and predicts its class label using nearest neighbor
        

class Classifier:
    def __init__(self, datasetWithOnlySubsetOfFeatures: List[List[float]]):

        self.datasetWithOnlySubsetOfFeatures = datasetWithOnlySubsetOfFeatures
        self.idToRowData = dict()


    def train(self, trainingInstanceIds: List[int]) -> None:
        
        for rowNumber in trainingInstanceIds:
            rowIndex = rowNumber - 1
            rowData: List[float] = self.datasetWithOnlySubsetOfFeatures[rowIndex]
            self.idToRowData[rowNumber] = rowData


    def test(self, test_instance : int) -> float:

        number_correctly_classfied = 0
        test_index = test_instance - 1

        label_of_object_to_classify = self.datasetWithOnlySubsetOfFeatures[test_instance-1][0]
        object_to_classify = self.datasetWithOnlySubsetOfFeatures[test_index][1:]
        
        
        numTrainingRows : int = len(self.idToRowData)

        nearestNeighborDistance = float('inf')
        nearestNeighborClass = float('inf')

        for key, value in self.idToRowData.items():
            classLabelForEachInstance = value[0]
            trainingDataForEachInstance = value[1:]

            distance = 0

            for i in range(len(trainingDataForEachInstance)):
                distance += math.pow((object_to_classify[i] - trainingDataForEachInstance[i]),2)

            distance = math.sqrt(distance)

            if distance < nearestNeighborDistance:
                nearestNeighborDistance = distance
                nearestNeighborClass = classLabelForEachInstance
        
        
        return nearestNeighborClass

    
            

            



        


inputData = [[2.0000, 1000,1000 ] , [2.0000, 100,100 ], [1.0000, 1,1 ] , [1.0000, 6.5,7.5 ]  ]

c = Classifier(inputData)
c.train([1,2,4])
print(c.test(3))
