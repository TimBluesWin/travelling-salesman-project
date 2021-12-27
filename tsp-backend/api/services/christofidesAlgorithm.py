import json
import os
from api.models import Point
import copy, random
import sys
from . import christofides


class SearchRouteAPI:
    def __init__(self):
        super().__init__()

    def christofidesCall(self, q):
        initialIndex = int(q) - 1
        path = os.path.dirname(__file__)
        file = open(path + '/matrix.json')
        data = json.load(file)
        matrix=[]
        for i in data:
            distances = []
            for distance in i:
                distances.append(float(distance))
            matrix.append(distances)
        file.close()
        newMatrix = self.convertMatrix(matrix)
        result = christofides.compute(newMatrix)
        initialTour = result['Christofides_Solution']

        properTour = self.getProperTour(initialIndex, initialTour)

        apiResult = self.getResults(matrix, properTour)

        return apiResult

    def getResults(self, matrix, tours):
        toursIndex = 0
        resultsList = []
        # raise Exception(tours)
        while toursIndex < len(tours):
            currentCity = tours[toursIndex]
            if toursIndex == 0:
                pointName = Point.objects.get(id=currentCity + 1)
                point = {
                    "id": currentCity + 1,
                    "name": pointName.name,
                    "distance": 0
                }
            else:
                pointName = Point.objects.get(id=currentCity + 1)
                point = {
                    "id": currentCity + 1,
                    "name": pointName.name,
                    "distance": matrix[currentCity - 1][currentCity]
                }
            resultsList.append(point)
            toursIndex = toursIndex + 1
        return resultsList

    def getProperTour(self, initialIndex, result):
        tour = []
        currentIndex = initialIndex
        while len(tour) < len(result):
            city = int(result[currentIndex])
            tour.append(city)
            if currentIndex == len(result) - 1:
                currentIndex = 0
            else:
                currentIndex = currentIndex + 1
        return tour

     # Because for the library that I use, there's a restriction of the distance matrix format.
    def convertMatrix(self, matrix):
        resultMatrix = copy.deepcopy(matrix)
        currentStartIndex = 0
        for startCity in matrix:
            currentEndIndex = 0
            for endCity in startCity:
                if currentStartIndex >= currentEndIndex:
                    resultMatrix[currentStartIndex][currentEndIndex] = 0
                currentEndIndex = currentEndIndex + 1
            currentStartIndex = currentStartIndex + 1
        return resultMatrix

def christofidesAlgorithm(q):
    api = SearchRouteAPI()
    return api.christofidesCall(q)