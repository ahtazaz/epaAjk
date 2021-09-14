from django.db import models

# Create your models here.
class Water(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    E_Coliform = models.IntegerField()
    Total_Coliform = models.IntegerField()
    Temperature = models.IntegerField()
    pH = models.IntegerField()
    Turbidity = models.IntegerField()
    Dissolved_Oxygen= models.IntegerField()
    Conductivity = models.IntegerField()
    Total_Dissolved_Solids =models.IntegerField()
    Total_Suspended_Solids = models.IntegerField()
    Total_Hardness = models.IntegerField()
    Biological_Oxygen_Demand= models.IntegerField()
    Aluminium = models.IntegerField()
    Boron= models.IntegerField()
    Chloride= models.IntegerField()
    Chromium= models.IntegerField()
    Copper= models.IntegerField()
    Cyanide= models.IntegerField()
    Fluoride = models.IntegerField()
    Lead= models.IntegerField()
    Manganese = models.IntegerField()
    Nickel = models.IntegerField()
    Nitrate = models.IntegerField()
    Nitrite= models.IntegerField()
    Chlorine = models.IntegerField()
    Zinc= models.IntegerField()
    COD = models.IntegerField()
    Sulphate = models.IntegerField()
    Sulphide = models.IntegerField()
    Cadmium= models.IntegerField()
    Nickle = models.IntegerField()
    Iron = models.IntegerField()
    Ammonium = models.IntegerField()
    Manganese = models.IntegerField()
    Phenol = models.IntegerField()


class Air(models.Model):
    date = models.DateTimeField()
    Carbon_Monoxide = models.IntegerField()
    NOx= models.IntegerField()
    SOx= models.IntegerField()
    Ozone = models.IntegerField()
    Particulate_Matter  = models.IntegerField()
    SOx = models.IntegerField()


class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    message = models.CharField(max_length=560)

class blog(models.Model):
    title = models.CharField(max_length=60)
    discription= models.CharField(max_length=50000)

class news(models.Model):
    new=models.CharField(max_length=560)
    date = models.DateTimeField(auto_now_add=True)