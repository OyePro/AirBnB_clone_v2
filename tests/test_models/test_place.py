#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models import *
import unittest
import os

db = os.getenv("HBNB_TYPE_STORAGE", 'fs')


class TestPlace(TestBasemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    @unittest.skipIf(db != "db", "test DBstorage only")
    def test_dbstorage(self):
        """ """
        user = User(email="joystick@nb.com", password="jspwd")
        user.save()
        state = State(name="Nevada")
        state.save()
        city = City(state_id=state.id, name="Las_Vegas")
        city.save()
        place = Place(user_id=user.id, city_id=city.id,
                      name="Fountains_of_Bellagio")
        place.save()
        self.assertTrue(type(place.latitude), None)
        self.assertTrue(type(place.longitude), None)
        self.assertTrue(type(place.description), None)
        self.assertEqual(type(place.max_guest), int)
