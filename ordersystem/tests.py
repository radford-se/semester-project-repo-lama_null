from unittest import skipIf

from django.test import TestCase

# Create your tests here.
from ordersystem.models import CustomerAccount, UserAccount, OrderSystem


class UserAccountTest(TestCase):
    def setUp(self):
        self.user1 = UserAccount(
            first_name="cust",
            last_name="one",
            username="custOne",
            email="cust1@test.com",
            password="1111")

    @skipIf(True, "Not finished")
    def test_customer_account_is_created(self):
        system = OrderSystem(customer=CustomerAccount())
        self.assertEqual(OrderSystem.objects.customer.all(), 1)

    def test_change_first_name(self):
        self.user1.change_first_name("customer")
        self.assertEqual(self.user1.first_name, "customer")

    def test_change_last_name(self):
        self.user1.change_last_name("ONE")
        self.assertEqual(self.user1.last_name, "ONE")