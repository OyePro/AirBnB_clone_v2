#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models import *
import unittest
import os

db = os.getenv("HBNB_TYPE_STORAGE", "fs")


class TestCity(TestBasemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipUnless(db != 'db', 'test filestorage only')
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipUnless(db != 'db', 'test filestorage only')
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipUnless(db == 'db', 'test DBstorage only')
    def test_dbstorage(self):
        """ """
        state = State(name="Nevada")
        state.save()
        city = City(name="Austin", state_id=state.id)
        city.save()
        self.assertEqual(city.state_id, state.id)

    @unittest.skipUnless(db == 'db', 'test DBstorage only')
    def test_id_dbstorage(self):
        """ """
        state = State(name="Nevada", id="fe234-6y5gg-u7y65")
        state.save()
        city = City(name="Beatty", state_id="fe234-6y5gg-u7y65")
        city.save()
        self.assertEqual(city.state_id, state.id)
