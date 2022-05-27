from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/add/', PostCreateView.as_view(), name='add'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update'),
]