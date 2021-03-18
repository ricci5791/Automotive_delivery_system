from django.db.models import QuerySet

from backend_api import models as api_models


class DatabaseAdapter:

    @staticmethod
    def get_drones_list():
        return api_models.Drone.objects.all()

    @staticmethod
    def get_owners_list():
        return api_models.Owner.objects.all()

    @staticmethod
    def get_recipients_list():
        return api_models.Recipient.objects.all()

    @staticmethod
    def get_orders_list():
        return api_models.Order.objects.all()

    @staticmethod
    def get_arrival(delivery_id: int) -> tuple[float, ...]:
        return tuple([float(x) for x in api_models.Order.objects.get(id=delivery_id).arrival_point.split(";")])

    @staticmethod
    def get_departure(delivery_id: int) -> tuple[float, ...]:
        return tuple([float(x) for x in api_models.Order.objects.get(id=delivery_id).departure_point.split(";")])

    @staticmethod
    def get_user_orders(recipient_token: int) -> QuerySet:
        return api_models.Order.objects.filter(recipient_token=recipient_token)

    @staticmethod
    def get_order_info(order_id: int) -> QuerySet:
        return api_models.Order.objects.get(id=order_id)

    @staticmethod
    def get_drones_by_status(status: str) -> QuerySet:
        return api_models.Drone.objects.filter(status=status)

    @staticmethod
    def get_available_drones() -> QuerySet:
        return api_models.Drone.objects.filter(status=api_models.Drone.IDLE)
