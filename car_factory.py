from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

# Assumptions are made about which models use which tires.

class CarFactory:
    @staticmethod
    def create_calliope(cur_date, last_service_date, cur_mileage, last_service_mileage, tire_status_arr):
        engine = CapuletEngine(cur_mileage, last_service_mileage)
        battery = SpindlerBattery(cur_date, last_service_date)
        tires = CarriganTires(tire_status_arr)
        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(cur_date, last_service_date, cur_mileage, last_service_mileage, tire_status_arr):
        engine = WilloughbyEngine(cur_mileage, last_service_mileage)
        battery = SpindlerBattery(cur_date, last_service_date)
        tires = OctoprimeTires(tire_status_arr)
        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(cur_date, last_service_date, warning_light_is_on, tire_status_arr):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(cur_date, last_service_date)
        tires = CarriganTires(tire_status_arr)
        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(cur_date, last_service_date, cur_mileage, last_service_mileage, tire_status_arr):
        engine = WilloughbyEngine(cur_mileage, last_service_mileage)
        battery = NubbinBattery(cur_date, last_service_date)
        tires = OctoprimeTires(tire_status_arr)
        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(cur_date, last_service_date, cur_mileage, last_service_mileage, tire_status_arr):
        engine = CapuletEngine(cur_mileage, last_service_mileage)
        battery = NubbinBattery(cur_date, last_service_date)
        tires = CarriganTires(tire_status_arr)
        return Car(engine, battery, tires)