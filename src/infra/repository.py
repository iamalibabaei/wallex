from abc import abstractmethod, ABC
from typing import List, Optional

from src.domain import Vending, VendingStatus


class VendingRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: str) -> Vending:
        pass

    @abstractmethod
    def get_by_status(self, status: VendingStatus) -> List[Optional[Vending]]:
        pass

    @abstractmethod
    def save(self, vending: Vending):
        pass


class InMemoryVendingRepository(VendingRepository):
    _vending_machines = {
        1: Vending(1, VendingStatus.IDLE, None,),
        2: Vending(2, VendingStatus.IDLE, None,),
        3: Vending(3, VendingStatus.IDLE, None,),
        4: Vending(4, VendingStatus.IDLE, None,),
    }

    def get_by_id(self, id: int) -> Vending:
        return self._vending_machines[id]

    def get_by_status(self, status: VendingStatus) -> List[Optional[Vending]]:
        res = []
        for vending_machine in self._vending_machines.values():
            if vending_machine.status == status:
                res.append(vending_machine)
        return res

    def save(self, vending: Vending):
        pass
