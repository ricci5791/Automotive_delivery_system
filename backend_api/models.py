from django.db import models


class Owner(models.Model):
    passport = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    account = models.UUIDField()


class Drone(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=20)
    lift_capacity = models.IntegerField()
    location = models.FloatField()
    charge = models.FloatField()
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)


class Recipient(models.Model):
    unique_token = models.CharField(primary_key=True, max_length=32)
    passport = models.IntegerField()
    full_name = models.CharField(max_length=100)


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    mass = models.FloatField()
    status = models.CharField(max_length=20)
    departure_point = models.CharField(max_length=30)
    arrival_point = models.CharField(max_length=30)
    aprox_arrival_time = models.DateTimeField()
    distance = models.FloatField()
    recipient_token = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    executor = models.ForeignKey(Drone, on_delete=models.DO_NOTHING)
