from tires.tires import Tires

SINGLE_TIRE_THRESHOLD = 0.9


class CarriganTires(Tires):
    def __init__(self, tire_status_arr):
        self.tire_status_arr = tire_status_arr

    def needs_service(self):
        for tire in self.tire_status_arr:
            if tire >= SINGLE_TIRE_THRESHOLD:
                return True
        return False
