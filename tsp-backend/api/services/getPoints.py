from django.core import serializers
from api.models import Point

class PointsAPI():
    def __init__(self):
        super().__init__()
    
    def search(self):
        resultList = []
        for e in Point.objects.all():
            point = {
                "id" : e.id,
                "name" : e.name
            }
            resultList.append(point)
        return resultList

def getPoints():
    api = PointsAPI()
    return api.search()