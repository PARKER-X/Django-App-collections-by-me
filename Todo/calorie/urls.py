from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('', FoodItemListView.as_view(), name="cal"),
    path('', views.index, name='indexy'),
    path('add/', FoodItemCreateView.as_view(), name='addfood'),
    path('<int:pk>/', FoodItemDetailView.as_view(), name='adddetail'),
    path('<int:pk>/delete', FoodItemDeleteView.as_view(), name='deleted'),
]
