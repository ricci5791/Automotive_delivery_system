from django.db import models


class Owner(models.Model):
    passport = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    account = models.UUIDField()


class Drone(models.Model):
    IDLE = "IDL"
    MOVING = "MOV"
    EXECUTING = "EXT"
    CHARGING = "CHG"
    DISABLED = "DIS"

    DRONE_STATUS_LIST = [
        (IDLE, "Idle"),
        (MOVING, "Moving"),
        (EXECUTING, "Executing"),
        (CHARGING, "Charging"),
        (DISABLED, "Disabled"),
    ]

    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=20, choices=DRONE_STATUS_LIST, default=IDLE)
    lift_capacity = models.IntegerField()
    location_x = models.FloatField()
    location_y = models.FloatField()
    charge = models.FloatField()
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)


class Recipient(models.Model):
    unique_token = models.CharField(primary_key=True, max_length=32)
    passport = models.IntegerField()
    full_name = models.CharField(max_length=100)


class Order(models.Model):
    INFO_RECEIVED = "REC"
    IN_TRANSIT = "TRN"
    OUT_OF_DELIVERY = "ODV"
    AVAILABLE_FOR_PICKUP = "APC"
    DELIVERED = "DLV"

    ORDER_STATUS_LIST = [
        (INFO_RECEIVED, "Information received"),
        (IN_TRANSIT, "In transit"),
        (OUT_OF_DELIVERY, "Out for delivery"),
        (AVAILABLE_FOR_PICKUP, "Available for pickup"),
        (DELIVERED, "Delivered"),
    ]

    id = models.IntegerField(primary_key=True)
    mass = models.FloatField()
    status = models.CharField(max_length=20, choices=ORDER_STATUS_LIST, default=INFO_RECEIVED)
    departure_point_x = models.FloatField()
    departure_point_y = models.FloatField()
    arrival_point_x = models.FloatField()
    arrival_point_y = models.FloatField()
    aprox_arrival_time = models.DateTimeField()
    distance = models.FloatField()
    recipient_token = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    executor = models.ForeignKey(Drone, on_delete=models.DO_NOTHING)
