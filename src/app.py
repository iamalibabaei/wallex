import datetime

from src.domain import VendingStatus
from src.infra.repository import InMemoryVendingRepository


class VendingApp:
    def __init__(self):
        self.repository = InMemoryVendingRepository()

    def insert_coin(self, id: int):
        vending = self.repository.get_by_id(id)
        vending.insert_coin()

        self.repository.save(vending)

    def submit_order(self, id: int):
        vending = self.repository.get_by_id(id)
        vending.purchase()
        self.repository.save(vending)

    def set_left_vending_to_idle(self):
        all_in_use_vendings = self.repository.get_by_status(VendingStatus.IN_USE)

        for vending in all_in_use_vendings:
            if (datetime.datetime.now() - vending.last_served_time).total_seconds() > 60:
                vending.status = VendingStatus.IDLE
                self.repository.save(vending)
