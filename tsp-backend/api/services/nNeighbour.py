from api.models import Point
import copy
import json, os


class SearchRouteAPI:
    def __init__(self):
        super().__init__()

    def nearestNeighbour(self, q):
        resultList = []
        path = os.path.dirname(__file__)
        file = open(path + '/matrix.json')
        data = json.load(file)
        matrix=[]
        for i in data:
            matrix.append(i)
        file.close()
        path = [int(q)]
        iteration, indicator = int(q) - 1, 0
        distance, pathCopy = [], copy.deepcopy(matrix)
        pointName = Point.objects.get(id=q)
        point = {"id": int(q), "name": pointName.name, "distance": 0}
        resultList.append(point)
        for j in range(1, len(matrix)):
            for x in range(len(matrix)):
                matrix[x][iteration] = 99999
            distance.append(min(matrix[iteration]))
            for i in range(len(matrix)):
                if min(matrix[iteration]) == matrix[iteration][i]:
                    indicator = i
                    minDistance = min(matrix[iteration])
            matrix[indicator][iteration] = 99999
            iteration = indicator
            pointName = Point.objects.get(id=indicator + 1)
            point = {
                "id": indicator + 1,
                "name": pointName.name,
                "distance": minDistance,
            }
            resultList.append(point)
            path.append(indicator + 1)
        path.append(int(q))
        a = pathCopy[path[-2] - 1][int(q) - 1]
        pointName = Point.objects.get(id=q)
        point = {"id": int(q), "name": pointName.name, "distance": a}
        resultList.append(point)
        # Add the results as well
        returnResults = {}
        returnResults['tour'] = resultList
        returnResults['distance'] = self.getDistance(resultList)
        return returnResults
    
    def getDistance(self, resultsList):
        totalDistance = 0
        for place in resultsList:
            currentDistance = place['distance']
            totalDistance = totalDistance + currentDistance
        return totalDistance


def nNeighbour(q):
    api = SearchRouteAPI()
    return api.nearestNeighbour(q)
