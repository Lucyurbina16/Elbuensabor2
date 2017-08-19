from django.db import models

# Create your models here.
class restaurant(models.Model):
    categories =(
    ('B','Breakfast'),
    ('L','Lunch'),
    ('Dn','Dinner'),
    ('Dr','Drinks'),
    ('D','Dessert')
    )
    title=models.CharField(max_length=60,help_text='Ingrese la descripcion del platillo:')
    typerestaurant=models.CharField(max_length=50,help_text='Que tipo de platillo desea:')
    price=models.CharField(max_length=50,help_text='El precio del platillo es:')
    time=models.CharField(max_length=50,help_text='El tiempo del platillo es:')
    category=models.CharField(max_length=1,help_text='Seleccione su platillo:')

class stock (models.Model):
    product=models.ForeignKey(restaurant)
    stock=models.IntegerField(help_text='Ingrese la cantidad de platillos:')
