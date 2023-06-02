from typing import List

def read_dataset(filename) -> List[List[float]]:
    data = []
    with open(filename, 'r') as file:
        for line in file:
            row = [float(num) for num in line.split()]
            data.append(row)
    return data


def filter_dataset(dataset, featureSet):
    filtered_data = []
    for row in dataset:
        filtered_row = [row[0]]  # Always include the 0th index
        filtered_row.extend(row[index] for index in featureSet if index != 0)
        filtered_data.append(filtered_row)
    return filtered_data



# Example usage
# dataset = [
#     [1.0, 2.3, 3.4, 4.5],
#     [1.0, 6.7, 7.8, 8.9],
#     [2.0, 1.1, 2.2, 3.3],
#     [2.0, 5.5, 6.6, 7.7]
# ]

# featureSet = [1, 2,4]

# filtered_dataset = filter_dataset(dataset, featureSet)
# print(filtered_dataset)
