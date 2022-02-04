import copy
def NearestNeighbour(matrix):
    source = input("Select source node -> ")
    path = [int(source)]
    iteration, indicator = int(source) -1, 0
    distance, pathCopy = [], copy.deepcopy(matrix)
    for j in range(1, len(matrix)):
        for x in range(len(matrix)):
            matrix[x][iteration] = 999
        distance.append(min(matrix[iteration]))
        for i in range(len(matrix)):
            if min(matrix[iteration]) == matrix[iteration][i]:
                indicator = i
        matrix[indicator][iteration] = 999
        path.append(indicator+1)
        iteration = indicator
    path.append(int(source))
    a = pathCopy[path[-2]-1][int(source)-1]
    distance.append(a)
    formatString = ""
    for item in path:
        formatString = formatString + str(item) + " -> "
    formatString = formatString[:-4]
    print("Objetive: "+ str(sum(distance)) + " miles")
    print('Route distance: {} miles\n'.format(formatString))
 
if __name__ == "__main__":
 
    # Matrix 
    graph = [[0, 25, 15, 45], [25, 0, 20, 35],
            [15, 20, 0, 30], [45, 35, 30, 0]]
    NearestNeighbour(graph)