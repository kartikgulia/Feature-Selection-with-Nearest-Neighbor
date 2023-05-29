from typing import List
import sys
import math

class Classifier:
    def __init__(self, datasetWithOnlySubsetOfFeatures: List[List[float]]):
        self.dataset = datasetWithOnlySubsetOfFeatures

        # access object's class label by doing :    self.idToClassLabelAndDataMap[rowNumber][0]
        # access object's data by doing        :    self.idToClassLabelAndDataMap[rowNumber][1]
        self.idToClassLabelAndDataMap = dict()

    def train(self, trainingInstanceIds: List[int]) -> None:
        
        for eachNum in trainingInstanceIds:
            rowNumber = eachNum
            classLabel = self.dataset[rowNumber-1][0]
            rowData: List[float] = self.dataset[rowNumber-1][1:]

            self.idToClassLabelAndDataMap[rowNumber] = classLabel , rowData


    def test(self, test_instance) -> float:
        number_correctly_classfied = 0
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
        
        
        return nearestNeighborClass

    
            

            



        


inputData = [[1.0000, 1000,1000 ] , [2.0000, 15.1,60 ], [1.0000, 1,1 ] , [2.0000, 6.5,7.5 ]  ]

c = Classifier(inputData)
c.train([1,2,4])
print(c.test(3))
