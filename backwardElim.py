from itertools import combinations
from randAccuracy import accuracy

def BE(featureNum):
    featureSet = set(range(1, featureNum + 1))
    bestSet = featureSet.copy()
    bestAcc = accuracy()

    print(f"Using all features and 'random' evaluation, I get an accuracy of: {bestAcc}%")
    print("Beginning Search")

    for i in range(featureNum, 0, -1):
        maxAcc = -float('inf')
        bestFeature = None

        for currentSet in combinations(featureSet, i - 1):
            temp = accuracy()
            print(f"Using feature(s) {currentSet}, accuracy is {temp}%")

            if temp > maxAcc:
                maxAcc = temp
                bestFeature = currentSet
                print(f"Feature(s) {currentSet} achieved the best accuracy: {maxAcc}%")
            else:
                print("Warning, accuracy decreased!")

        if maxAcc > bestAcc:
            bestAcc = maxAcc
            bestSet = set(bestFeature)
        else:
            break

    print(f"\nBest feature subset: {bestSet}")
    print(f"Best accuracy: {bestAcc}%")
