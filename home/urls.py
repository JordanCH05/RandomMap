from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('map/<map_id>', views.map, name='map'),
]
