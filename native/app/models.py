from django.db import models

# Django models describe the layout of our project's database.
# Each model is a Python class that's usually mapped to a database table.
# The class properties are mapped to the database's columns.

from django.db import models

class Host(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    guestLimit = models.IntegerField(null=True, blank=True)
    photo = models.SlugField(max_length=100, blank=True)
    rating = models.IntegerField(null=True, blank=True)

class Traveler(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, blank=True)

class Trip(models.Model):
    traveler_id = models.ForeignKey(Traveler, on_delete=models.SET_NULL, null=True, blank=True)
    host_id = models.ForeignKey(Host, on_delete=models.CASCADE)
    interest = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    guests = models.IntegerField(blank=True, null=True)

class Review(models.Model):
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    host_id = models.ForeignKey(Host, on_delete=models.CASCADE)
    traveler_id = models.ForeignKey(Traveler, on_delete=models.SET_NULL, null=True, blank=True)
