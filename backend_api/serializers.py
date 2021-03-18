from rest_framework import serializers
from backend_api import models as api_models


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Drone
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Order
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Owner
        fields = "__all__"


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Recipient
        fields = "__all__"
