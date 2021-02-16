from django.urls import path
from .views import *

app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('list/', CarListView.as_view()),
    path('car/detail/<int:pk>', CarDetailView.as_view()),
]