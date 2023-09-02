from engine.engine import Engine

SERVICE_INTERVAL = 60000  # miles


class WilloughbyEngine(Engine):
    def __init__(self, cur_mileage, last_service_mileage):
        self.cur_mileage = cur_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.cur_mileage - self.last_service_mileage > SERVICE_INTERVAL
