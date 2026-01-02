from django.urls import path
from .views import project_manager_view

urlpatterns = [
    path('projects/', project_manager_view, name='project-list'),
    path('projects/<int:pk>/', project_manager_view, name='project-detail'),
]