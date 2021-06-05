from django.urls import path, include
from auto.views import CarView

urlpatterns = [
    path('', CarView.as_view(), name='index'),
]