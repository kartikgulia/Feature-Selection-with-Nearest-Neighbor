import matplotlib.pyplot as plt
from Validator import Validator
def plotTraceGraph(featureSubset, fileName):
  
    data = []
    with open(fileName, 'r') as file:
        for line in file:
            row = line.strip().split()
            data.append(row)


    x_values = [float(row[featureSubset[0]]) for row in data]
    y_values = [float(row[featureSubset[1]]) for row in data]
    classes = [float(row[0]) for row in data]


    for x, y, class_value in zip(x_values, y_values, classes):
        if class_value == 1.0:
            plt.scatter(x, y, color='red')
        elif class_value == 2.0:
            plt.scatter(x, y, color='blue')

  
    plt.xlabel(f'Feature {featureSubset[0]}')
    plt.ylabel(f'Feature {featureSubset[1]}')
    plt.title('Small Personal Dataset')
    plt.show()




