import copy
from Validator import Validator


def BE(featureNum, textfileName):
  bestSet = list(range(1, featureNum + 1))
  bestAcc = 0.0
  currSet = bestSet.copy()
  print("Beginning Search.")

  if featureNum == 1:
    print("Using feature(s) [1] accuracy is", bestAcc, "%")
    print(
      "Warning: Accuracy cannot be improved further by removing any feature!")
    print(
      "Finished Search! The best feature subset is [1] which has an accuracy of",
      bestAcc, "%")
    return

  for i in range(featureNum - 1, 0, -1):
    currAcc = 0.0
    featureToRemove = -1
    for j in range(1, featureNum + 1):
      if j in currSet:
        node = copy.deepcopy(currSet)
        node.remove(j)
        v: Validator = Validator(node, textfileName)
        temp = v.calculate_accuracy()
        print(f"Using feature(s) {sorted(node)} accuracy is {temp}%")
        if temp > currAcc:
          currAcc = temp
          featureToRemove = j
    if currAcc > bestAcc:
      currSet.remove(featureToRemove)
      bestSet = currSet.copy()
      bestAcc = currAcc
      print(f"Feature set {sorted(currSet)} was best, accuracy is {bestAcc}%")
    elif currAcc < bestAcc:
      currSet.remove(featureToRemove)
      print(f"Feature set {sorted(currSet)} was best, accuracy is {currAcc}%")
    else:
      print(
        f"Warning: Accuracy cannot be improved further by removing any feature!"
      )
      break

  if not bestSet:
    print("Warning: Empty feature set!")
  print(
    f"Finished Search! The best feature subset is {bestSet} which has an accuracy of {bestAcc}%"
  )
