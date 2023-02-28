import unittest

import exceptions
from src.domain import Vending, VendingStatus


class TestVending(unittest.TestCase):

    def test_insert_coin(self):
        vending = Vending(1, VendingStatus.IDLE, None)
        vending.insert_coin()
        self.assertEqual(vending.status, VendingStatus.IN_USE)
        self.assertIsNotNone(vending.last_served_time)

    def test_insert_coin_on_an_in_use_vending(self):
        vending = Vending(1, VendingStatus.IDLE, None)
        vending.insert_coin()
        self.assertEqual(vending.status, VendingStatus.IN_USE)
        self.assertIsNotNone(vending.last_served_time)

        with self.assertRaises(exceptions.VendingAlreadyInUseException):
            vending.insert_coin()

    def test_purchase(self):
        vending = Vending(1, VendingStatus.IDLE, None)
        vending.insert_coin()
        self.assertEqual(vending.status, VendingStatus.IN_USE)
        self.assertIsNotNone(vending.last_served_time)
        vending.purchase()
        self.assertEqual(vending.status, VendingStatus.IDLE)

    def test_purchase_without_insertion(self):
        vending = Vending(1, VendingStatus.IDLE, None)
        with self.assertRaises(exceptions.NoCoinInserted):
            vending.purchase()
