from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework import permissions

from backend_api.databaseadapter import DatabaseAdapter
from backend_api import serializers
from backend_api.pathfinder import Path


class DroneListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = DatabaseAdapter.get_drones_list()
    serializer_class = serializers.DroneSerializer


class OwnerListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = DatabaseAdapter.get_owners_list()
    serializer_class = serializers.OwnerSerializer


class RecipientListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = DatabaseAdapter.get_recipients_list()
    serializer_class = serializers.RecipientSerializer


class OrderListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = DatabaseAdapter.get_orders_list()
    serializer_class = serializers.OrderSerializer


class AvailableDronesList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = DatabaseAdapter.get_available_drones()
    serializer_class = serializers.DroneSerializer


class PathAlgoView(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        order_id = int(request.query_params.get("order_id"))
        path = Path(order_id)

        return Response(data=path._Path__choose_optimal_drone(), status=status.HTTP_200_OK)
