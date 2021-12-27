from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import views, status
import abc
from .services.nNeighbour import nNeighbour
from .services.rInsertion import rInsertion
from .services.getPoints import getPoints
from .services.googleOr import googleOr
from .services.cheapestInsertion import cheapestInsertion
from .services.christofidesAlgorithm import christofidesAlgorithm

class ThroughAPIBaseView(views.APIView):
    response_viewset = None

    @abc.abstractmethod
    def get_token(self, *args, **kwargs):
        return None

    def get(self, request, *args, **kwargs):
        params = self.request.query_params.dict()
        response = {}
        if self.response_viewset:
            response = self.response_viewset.as_view()(
                request=request._request, *args, **kwargs
            ).data
        return Response(response, status=status.HTTP_200_OK)


class PointView(ThroughAPIBaseView):
    def get(self, request):
        words = getPoints()
        return JsonResponse(words, safe=False)

class NNeighbourView(ThroughAPIBaseView):
    def get(self, request):
        search = request.GET.get('q')
        words = nNeighbour(search)
        return JsonResponse(words, safe=False)

class RandomView(ThroughAPIBaseView):
    def get(self, request):
        search = request.GET.get('q')
        words = rInsertion(search)
        return JsonResponse(words, safe=False)

class GoogleOrView(ThroughAPIBaseView):
    def get(self, request):
        search = request.GET.get('q')
        words = googleOr(search)
        return JsonResponse(words, safe=False)

class CheapestInsertionView(ThroughAPIBaseView):
    def get(self, request):
        search = request.GET.get('q')
        words = cheapestInsertion(search)
        return JsonResponse(words, safe=False)

class ChristofidesAlgorithmView(ThroughAPIBaseView):
    def get(self, request):
        search = request.GET.get('q')
        words = christofidesAlgorithm(search)
        return JsonResponse(words, safe=False)