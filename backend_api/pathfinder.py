import math

from django.db.models import QuerySet

from backend_api.databaseadapter import DatabaseAdapter as db_adapter


class Path:

    def __init__(self, delivery_id: int):
        self.departure = db_adapter.get_departure(delivery_id)
        self.arrival = db_adapter.get_arrival(delivery_id)
        self.path_length = self.__get_path_length()

    def __get_path_length(self) -> float:
        X, Y = zip(self.arrival, self.departure)
        x, y = X[0] - X[1], Y[0] - Y[1]

        x, y = (X[0] - X[1]) ** 2, (Y[0] - Y[1]) ** 2

        return math.sqrt(x + y)

    def choose_optimal_drone(self) -> int:
        x_diff, y_diff = math.inf, math.inf
        temp_x, temp_y = 0., 0.
        nearest_drone_id = None

        for drone in db_adapter.get_available_drones():
            drone_coords = db_adapter.get_drone_coords(drone)
            temp_x = drone_coords[0] - self.departure[0]
            temp_y = drone_coords[1] - self.departure[1]

            if temp_x < x_diff or temp_y < y_diff:
                nearest_drone_id = drone.id
                x_diff = temp_x
                y_diff = temp_y

        return nearest_drone_id
