import json
import os
from api.models import Point
import copy, random
import sys


class SearchRouteAPI:
    def __init__(self):
        super().__init__()

    def cheapestInsertionFirstStepResults(self, matrix, sourceIndex):
        dictionaryInfo = {}
        usedDistanceMatrix = matrix[sourceIndex]

        smallestDistance = sys.maxsize * 2
        bestIndex = None
        currentIndex = 0
        for distance in usedDistanceMatrix:
            if currentIndex == sourceIndex:
                currentIndex = currentIndex + 1
                continue
            if distance < smallestDistance:
                smallestDistance = distance
                bestIndex = currentIndex
            currentIndex = currentIndex + 1
        dictionaryInfo['index'] = bestIndex
        dictionaryInfo['distance'] = smallestDistance
        return dictionaryInfo

    def cheapestInsertionAlgorithm(self, q):
        q = int(q)-1
        resultList = []
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

        numberOfData = len(matrix)
        pathCopy = copy.deepcopy(matrix)

        # When we insert a city to the tour, we append that city to tours variable.
        tours = []
        tours.append(int(q))
        firstStepResult = self.cheapestInsertionFirstStepResults(pathCopy, (int(q)))
        tours.append(firstStepResult['index'])

        cityNumber = 3
        # If the number of nodes in tour < number of cities, keep looping.
        while(len(tours) < numberOfData):
            # We want to iterate each node that hasn't been visited.
            currentCityIndex = 0
            currentAddedCity = None
            currentPreviousCity = None
            currentNextCity = None
            currentAddedCost = sys.maxsize * 2
            bestAddedCity = None
            bestPreviousCity = None
            bestNextCity = None
            bestAddedCost = sys.maxsize * 2

            # represents the origin city from the provided matrix.
            for originCity in pathCopy:
                # Skip if already in tour.
                if currentCityIndex in tours:
                    currentCityIndex = currentCityIndex + 1
                    continue
                # Iterate each subtour
                currentAddedCity = currentCityIndex
                cityIndex = 0
                for city in tours:
                    # if it is last, pair it with the first.
                    if city == tours[-1]:
                        currentPreviousCity = city
                        currentNextCity = tours[0]
                    else:
                        currentPreviousCity = tours[cityIndex]
                        currentNextCity = tours[cityIndex + 1]
                    # We start to compare the costs of adding the 
                    cityIndex = cityIndex + 1
                    currentAddedCost = pathCopy[currentPreviousCity][currentAddedCity] + pathCopy[currentAddedCity][currentNextCity] - pathCopy[currentPreviousCity][currentNextCity]
                    if currentAddedCost < bestAddedCost:
                        bestAddedCost = currentAddedCost
                        bestPreviousCity = currentPreviousCity
                        bestNextCity = currentNextCity
                        bestAddedCity = currentAddedCity

                currentCityIndex = currentCityIndex + 1
            # add city to the variable tour.
            previousCityIndex = tours.index(bestPreviousCity)
            tours.insert(previousCityIndex + 1, bestAddedCity)
            cityNumber = cityNumber + 1
        tours.append(int(q))
        resultList = self.generateResults(matrix, tours)
        return resultList
        # Then we want to return the results from the API.

    def generateResults(self, matrix, tours):
        returnResults = {}
        toursIndex = 0
        resultsList = []
        # raise Exception(tours)
        while toursIndex < len(tours):
            
            if toursIndex == 0:
                currentCity = tours[toursIndex]
                pointName = Point.objects.get(id=currentCity + 1)
                point = {
                    "id": currentCity + 1,
                    "name": pointName.name,
                    "distance": 0
                }
            else:
                currentCity = tours[toursIndex]
                previousCity = tours[toursIndex - 1]
                pointName = Point.objects.get(id=currentCity + 1)
                point = {
                    "id": currentCity + 1,
                    "name": pointName.name,
                    "distance": matrix[previousCity][currentCity]
                }
            resultsList.append(point)
            toursIndex = toursIndex + 1
        returnResults['tour'] = resultsList
        returnResults['distance'] = self.getDistance(resultsList)
        return returnResults

    def getDistance(self, resultsList):
        totalDistance = 0
        for place in resultsList:
            currentDistance = place['distance']
            totalDistance = totalDistance + currentDistance
        return totalDistance


def cheapestInsertion(q):
    api = SearchRouteAPI()
    return api.cheapestInsertionAlgorithm(q)
