from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory:
    @staticmethod
    def create_calliope(cur_date, last_service_date, cur_mileage, last_service_mileage):
        engine = CapuletEngine(cur_mileage, last_service_mileage)
        battery = SpindlerBattery(cur_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(cur_date, last_service_date, cur_mileage, last_service_mileage):
        engine = WilloughbyEngine(cur_mileage, last_service_mileage)
        battery = SpindlerBattery(cur_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(cur_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(cur_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(cur_date, last_service_date, cur_mileage, last_service_mileage):
        engine = WilloughbyEngine(cur_mileage, last_service_mileage)
        battery = NubbinBattery(cur_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(cur_date, last_service_date, cur_mileage, last_service_mileage):
        engine = CapuletEngine(cur_mileage, last_service_mileage)
        battery = NubbinBattery(cur_date, last_service_date)
        return Car(engine, battery)