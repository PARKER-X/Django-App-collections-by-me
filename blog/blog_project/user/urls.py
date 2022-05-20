from django.contrib import admin
from django.urls import path, include
from .views import *
from user import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inde , name='inde'),
    path('login/', views.userlogin, name = 'login'),
    path('logout/', views.userlogout, name = 'logout'),
]
