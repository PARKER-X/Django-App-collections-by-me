from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=50)
    carbs = models.FloatField()
    protein = models.FloatField()
    Calorie = models.FloatField()
    fat  = models.FloatField()
    
    def __str__(self):
        return self.name

    
    