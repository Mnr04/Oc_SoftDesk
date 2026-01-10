from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

router = DefaultRouter()

router.register('projects', ProjectViewSet, basename='project')
routee.register('contributors', ContributorViewSet, basename='contributor')

urlpatterns = [
    path('', include(router.urls)),
]