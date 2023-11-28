#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models import *
import unittest
import os

db = os.getenv("HBNB_TYPE_STORAGE", "fs")


class TestReview(TestBasemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @unittest.skipUnless(db != "db", "test filestorage only")
    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    @unittest.skipUnless(db != "db", "test filestorage only")
    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipUnless(db != "db", "test filestorage only")
    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    @unittest.skipUnless(db == "db", "test DBstorage only")
    def test_dbstorage(self):
        """ """
        state = State(name="Nevada")
        state.save()
        city = City(state_id=state.id, name="Las_Vegas")
        city.save()
        user = User(email="unknown@mail.com", password="knownpwd")
        user.save()
        place = Place(user_id=user.id, city_id=city.id, name="Bellagio")
        place.save()
        review = Review(place_id=place.id, user_id=user.id,
                        text="Amazing place, huge kitchen")
        review.save()
        self.assertEqual(place.user_id, review.user_id)
        self.assertNotEqual(review.created_at, review.updated_at)
        self.assertTrue(type(review.text) is str)
        self.assertNotEqual(review.place_id, review.id)
