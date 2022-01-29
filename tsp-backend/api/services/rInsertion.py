import json
import os
from api.models import Point
import copy, random


class SearchRouteAPI:
    def __init__(self):
        super().__init__()

    def randomInsertion(self, q):
        q = int(q)-1
        resultList = []
        path = os.path.dirname(__file__)
        file = open(path + '/matrix.json')
        data = json.load(file)
        matrix=[]
        for i in data:
            matrix.append(i)
        file.close()
        for item in matrix:
            item.append(False)
        newMatrix = []
        newMatrix.append(int(q))
        matrix[int(q)][-1] = True
        while len(matrix) > len(newMatrix):
            rand = random.randint(0, len(matrix) - 1)
            if matrix[rand][-1] == False:
                newMatrix.append(rand)
                matrix[rand][-1] = True
        newMatrix.append(int(q))
        count = 0
        for item in newMatrix:
            item = item + 1
            if count == 0:
                pointName = Point.objects.get(id=item)
                point = {"id": int(item), "name": pointName.name, "distance": 0}
                resultList.append(point)
                count = count + 1
                continue
            pointName = Point.objects.get(id=item)
            position = newMatrix[count-1]
            dist = matrix[position][item-1]
            point = {"id": item, "name": pointName.name, "distance": dist}
            resultList.append(point)
            count = count + 1
        
        # Add the results as well
        returnResults = {}
        returnResults['tour'] = resultList
        returnResults['distance'] = self.getDistance(resultList)
        return returnResults
            
        return resultList

    def getDistance(self, resultsList):
        totalDistance = 0
        for place in resultsList:
            currentDistance = place['distance']
            totalDistance = totalDistance + currentDistance
        return totalDistance

def rInsertion(q):
    api = SearchRouteAPI()
    return api.randomInsertion(q)
