from .views import api_home
from django.urls import path,include
 
urlpatterns = [
  path('api/',api_home),
]