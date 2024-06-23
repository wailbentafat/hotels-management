from django.urls import path
from . import views

urlpatterns = [
    path('add_client/', views.add_client, name="add_client"),
    path('delete_client/<str:name>/', views.delete_client, name="delete_client"),
    path('get_empty_room/', views.get_empty_room, name="get_empty_room"),
    path('add_room/', views.add_room, name="add_room"),
]
