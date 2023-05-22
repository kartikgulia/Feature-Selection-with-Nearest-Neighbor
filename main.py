from randAccuracy import accuracy
import sys
from backwardElim import BE
from forwardSelection import FS

print("Welcome to Group 31's Feature Select Algorithm")

print("Please enter total numbers of features:")
featureNum = int(input())

print("Type the number of the algorithm you want to run.\n 1. Forward Selection \n 2. Backward Elimination ")
algoNum = int(input())

#print(f"test {algoNum}")
if algoNum == 1:
	#print("testtttttt")
	FS(featureNum)
elif (algoNum == 2):
	BE(featureNum)
else:
	print("Invalid Input")
	sys.exit()




