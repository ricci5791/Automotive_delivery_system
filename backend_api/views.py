from rest_framework import generics, views, status
from rest_framework.response import Response

from backend_api.databaseadapter import DatabaseAdapter
from backend_api import serializers
from backend_api.pathfinder import Path


class DroneListView(generics.ListAPIView):
    queryset = DatabaseAdapter.get_drones_list()
    serializer_class = serializers.DroneSerializer


class OwnerListView(generics.ListAPIView):
    queryset = DatabaseAdapter.get_owners_list()
    serializer_class = serializers.OwnerSerializer


class RecipientListView(generics.ListAPIView):
    queryset = DatabaseAdapter.get_recipients_list()
    serializer_class = serializers.RecipientSerializer


class OrderListView(generics.ListAPIView):
    queryset = DatabaseAdapter.get_orders_list()
    serializer_class = serializers.OrderSerializer
