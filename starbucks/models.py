from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = "menu"

class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = "category"

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=5, decimal_places=1)
    sodium_mg = models.DecimalField(max_digits=5, decimal_places=1)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=1)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=1)
    protein_g = models.DecimalField(max_digits=5, decimal_places=1)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        db_table = "nutrition_info"

class Drink(models.Model):
    category_id = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    nutrition = models.ForeignKey(Nutrition, on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = "nutrition_information"

class Image(models.Model):
    image_url = models.URLField(max_length=2000)
    drink = models.ForeignKey(Drink, on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = "images"

class Description(models.Model):
    drink = models.ForeignKey(Drink, on_delete = models.SET_NULL, null=True)
    description = models.TextField()

    class Meta:
        db_table = "description"

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "allergy"

class AllergyDrink(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete = models.SET_NULL, null=True)
    drink = models.ForeignKey(Drink, on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = "allergy_drink"

class Size(models.Model):
    nutrition = models.ForeignKey(Nutrition, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length=45)
    size_ml = models.IntegerField(default=0)
    size_fluid_ounce = models.IntegerField(default=0)

    class Meta:
        db_table = "size"










# Create your models here.
