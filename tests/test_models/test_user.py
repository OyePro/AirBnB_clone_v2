#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.user import User
import os
import unittest

db = os.getenv("HBNB_TYPE_STORAGE", 'fs')


class TestUser(TestBasemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @unittest.skipUnless((db != 'db'), "test filestorage only")
    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    @unittest.skipUnless((db != 'db'), "test filestorage only")
    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    @unittest.skipUnless((db != 'db'), "test filestorage only")
    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    @unittest.skipUnless((db != 'db'), "test filestorage only")
    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    @unittest.skipIf((db != 'db'), "test DBStorage only")
    def test_db_storage(self):
        """ """
        user = User(email="oyepro@gmail.com", password="oyepropwd")
        user.save()
        self.assertEqual(user.email, "oyepro@gmail.com")

    @unittest.skipIf((db != 'db'), "test DBStorage only")
    def test_id_dbstorage(self):
        """ """
        user1 = User(email="john@snow.com", password="johnpwd")
        user1.save()
        user2 = User(email="ghbdudu@bn.com", password="hgt5677")
        user2.save()
        self.assertNotEqual(user1.id, user2.id)
