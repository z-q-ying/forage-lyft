from battery.battery import Battery
from dateutil.relativedelta import relativedelta

SERVICE_INTERVAL = 3  # years


class SpindlerBattery(Battery):
    def __init__(self, cur_date, last_service_date):
        self.cur_date = cur_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_due_date = self.last_service_date + relativedelta(years=SERVICE_INTERVAL)
        return self.cur_date >= service_due_date
