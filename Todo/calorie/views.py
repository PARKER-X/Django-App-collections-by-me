from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from .models import *
from django.db.models import Sum
from django.urls import reverse_lazy

# Create your views here.
# class FoodItemListView(ListView):
#     model = FoodItem
    
#     s = FoodItem.objects.aggregate(Sum('carbs'))

    
#     template_name = "calorie/index.html"
    
def index(request):
    model =FoodItem.objects.all()
    carbs  = FoodItem.objects.aggregate(Sum('carbs'))
    protein = FoodItem.objects.aggregate(Sum('protein'))
    Calorie = FoodItem.objects.aggregate(Sum('Calorie'))
    fat = FoodItem.objects.aggregate(Sum('fat'))
    
    return render(request, 'calorie/index.html', {'object_list':model, 'carbs':carbs['carbs__sum'],'protein':protein['protein__sum'],'Calorie':Calorie['calorie__sum'], 'fat':fat['fat__sum']})

class FoodItemCreateView(CreateView):
    model = FoodItem
    template_name = "calorie/add.html"
    fields='__all__'

class FoodItemDeleteView(DeleteView):
    model = FoodItem
    template_name = "calorie/delete.html"
    success_url = reverse_lazy('indexy')

class FoodItemDetailView(DetailView):
    model = FoodItem
    template_name = "calorie/detail.html"
