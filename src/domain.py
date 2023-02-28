import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from dataclasses_json import dataclass_json

from src.exceptions import VendingAlreadyInUseException, NoCoinInserted


class VendingStatus(Enum):
    IDLE = 'IDLE'
    IN_USE = 'IN_USE'


@dataclass_json
@dataclass
class Vending:
    id: int
    status: VendingStatus
    last_served_time: Optional[datetime.datetime]

    def insert_coin(self):
        if self.status == VendingStatus.IN_USE:
            raise VendingAlreadyInUseException()

        self.status = VendingStatus.IN_USE
        self.last_served_time = datetime.datetime.now()

    def purchase(self):
        if self.status != VendingStatus.IN_USE:
            raise NoCoinInserted()

        self.status = VendingStatus.IDLE
