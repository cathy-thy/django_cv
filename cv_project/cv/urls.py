from django.urls import path
from .views import cv_view

# URL patterns for the 'cv' application
urlpatterns = [
    # Route for the CV view
    path('', cv_view, name='cv'),
]