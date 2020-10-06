from dataclasses import field
from unittest import TestCase
import forms
from models import User


class Test(TestCase, field):
    def test_name_exists(self):
        return field.data(User.username)
        self.fail()


class Test(TestCase):
    def test_email_exists(self):
        return field.data(User.email)
        self.fail()
