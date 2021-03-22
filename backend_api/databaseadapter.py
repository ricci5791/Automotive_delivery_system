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
    def get_arrival(order_id: int) -> tuple[float, float]:
        order = api_models.Order.objects.get(id=order_id)
        return order.arrival_point_x, order.arrival_point_y

    @staticmethod
    def get_departure(order_id: int) -> tuple[float, float]:
        order = api_models.Order.objects.get(id=order_id)
        return order.departure_point_x, order.departure_point_y

    @staticmethod
    def get_user_orders(recipient_token: int) -> QuerySet:
        return api_models.Order.objects.filter(recipient_token=recipient_token)

    @staticmethod
    def get_order_info(order_id: int) -> QuerySet:
        return api_models.Order.objects.get(id=order_id)

    @staticmethod
    def get_available_drones() -> QuerySet:
        return api_models.Drone.objects.filter(status=api_models.Drone.IDLE)

    @staticmethod
    def set_drone_to_order(order_id: int, drone_id: int) -> bool:
        order = api_models.Order.objects.get(id=order_id)
        drone = api_models.Drone.objects.get(id=drone_id)

        order.executor = drone
        order.save()

        drone.status = api_models.Drone.EXECUTING
        drone.save()
        return True

    @staticmethod
    def release_drone(drone_id: int) -> bool:
        drone = api_models.Drone.objects.get(id=drone_id)
        drone.status = api_models.Drone.IDLE
        return True

    @staticmethod
    def charge_drone(drone_id: int) -> bool:
        drone = api_models.Drone.objects.get(id=drone_id)
        drone.status = api_models.Drone.IDLE
        return True

    @staticmethod
    def get_drone_coords(drone: api_models.Drone) -> tuple[float, float]:
        return drone.location_x, drone.location_y
