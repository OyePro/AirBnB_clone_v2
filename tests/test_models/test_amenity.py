#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models import *
import os
import unittest
import MySQLdb

dbenv = os.getenv("HBNB_TYPE_STORAGE", "fs")


class TestAmenity(TestBasemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @classmethod
    def setUp(cls):
        """Starting MySQL connector"""
        cls.db = MySQLdb.connect(host="localhost", user="hbnb_dev",
                                 passwd="hbnb_dev_pwd", db="hbnb_dev_db")
        cls.cursor = cls.db.cursor()

    @classmethod
    def tearDown(cls):
        """Close the MySQL connection"""
        cls.cursor.close()
        cls.db.close()

    @unittest.skipIf(dbenv == 'db', "for filestorage only")
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(dbenv != 'db', 'for DBStorage only')
    def test_review_dbstorage(self):
        """ """
        amenity1 = Amenity(name="WiFi")
        amenity1.save()
        amenity2 = Amenity(name="Cable")
        amenity2.save()
        self.assertEqual(amenity1.name, "WiFi")
        self.assertNotEqual(amenity2.id, amenity1.id)

    @unittest.skipIf(dbenv != 'db', 'for DBStorage only')
    def test_place_amenity_dbstorage(self):
        """Testing relationship of place with amenity"""

        user = User(email="joystick@nb.com", password="jspwd")
        user.save()
        state = State(name="Nevada")
        state.save()
        city = City(state_id=state.id, name="Las_Vegas")
        city.save()

        """creating instances of place"""
        place1 = Place(user_id=user.id, city_id=city.id,
                       name="Fountains_of_Bellagio")
        place1.save()
        place2 = Place(user_id=user.id, city_id=city.id, name="Bellagio")
        place2.save()

        """creating instances of amenity"""
        amenity1 = Amenity(name="Laserjet")
        amenity1.save()
        amenity2 = Amenity(name="Desktop")
        amenity2.save()
        amenity3 = Amenity(name="Laptop")
        amenity3.save()

        """counting the rows of in place_amenity table before adding"""
        query = f"SELECT COUNT(*) FROM place_amenity;"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        count = result[0]

        """linking place1 with 2 amenities"""
        place1.amenities.append(amenity1)
        place1.amenities.append(amenity2)

        """linking place2 with 3 amenities"""
        place2.amenities.append(amenity1)
        place2.amenities.append(amenity2)
        place2.amenities.append(amenity3)

        storage.save()

        """counting the rows after adding"""
        query = f"SELECT COUNT(*) FROM place_amenity;"
        self.cursor.execute(query)
        result1 = self.cursor.fetchone()
        count1 = result1[0]

        self.assertTrue(count1 == count)
