from django.db.models import QuerySet

from backend_api import models as api_models


class DatabaseAdapter:

    @staticmethod
    def get_arrival(delivery_id: int) -> tuple[float, ...]:
        return tuple([float(x) for x in api_models.Order.objects.get(id=delivery_id).arrival_point.split(";")])

    @staticmethod
    def get_departure(delivery_id: int) -> tuple[float, ...]:
        return tuple([float(x) for x in api_models.Order.objects.get(id=delivery_id).departure_point.split(";")])

    @staticmethod
    def get_user_orders(recipient_token: int) -> QuerySet:
        return api_models.Order.objects.get(recipient_token=recipient_token)

    @staticmethod
    def get_order_info(order_id: int) -> QuerySet:
        return api_models.Order.objects.get(id=order_id)
