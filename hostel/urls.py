from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<int:item_id>/', views.room_details, name='room_detail'),
    path('facilities/', views.facilities, name='facilities'),
]
