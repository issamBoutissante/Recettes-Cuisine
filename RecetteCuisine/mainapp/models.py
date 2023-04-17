from django.db import models

# Create your models here.


class Category(models.Model):
    label = models.CharField(max_length=50)


class Recipe(models.Model):
    title = models.TextField
    description = models.TextField
    duration = models.IntegerField
    nbrPersons = models.IntegerField
    nbrCalories = models.IntegerField
    difficulty = models.IntegerField
    categories = models.ManyToManyField(Category)


class Ingredient(models.Model):
    description = models.TextField
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Step(models.Model):
    descreption = models.TextField
    number = models.IntegerField
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class User(models.Model):
    email = models.TextField
    password = models.TextField


class Comment(models.Model):
    text = models.TextField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Rating(models.Model):
    rate = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
