from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator
#models are tables
# Create your models here.
class Lib_Customers(models.Model):#models is creating and modle is importing and  inherting
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age=models.IntegerField(validators=[MinLengthValidator(1),MaxLengthValidator(100)])

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old customer'
    #To run table python ma

