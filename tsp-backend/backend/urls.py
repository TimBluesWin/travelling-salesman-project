from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework import routers
from django.contrib import admin
from api.views import PointView, NNeighbourView, RandomView

router = routers.DefaultRouter()
# router.register(r'authors',  AuthorsViewSet, basename='users_set')

urlpatterns = router.urls

# add regular views to the urlpatterns array
urlpatterns += [
    path("api/nneighbour/", NNeighbourView.as_view(), name="nneighbour"),
    path("api/rinsertion/", RandomView.as_view(), name="rinsertion"),
    path("api/points/", PointView.as_view(), name="points"),
    path('admin/', admin.site.urls),
]