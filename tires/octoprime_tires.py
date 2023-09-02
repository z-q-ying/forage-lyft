from tires.tires import Tires

FOUR_TIRES_THRESHOLD = 3.0


class OctoprimeTires(Tires):
    def __init__(self, tire_status_arr):
        self.tire_status_arr = tire_status_arr

    def needs_service(self):
        return sum(self.tire_status_arr) >= FOUR_TIRES_THRESHOLD
