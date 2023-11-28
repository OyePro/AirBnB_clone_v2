#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBasemodel
from models.state import State
import os
import unittest

db = os.getenv("HBNB_TYPE_STORAGE", "fs")


class TestState(TestBasemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skipIf(db == "db", "test filestorage only")
    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(db != "db", "test dbstorage only")
    def test_dbstorage(self):
        """ """
        state = State(name="California")
        state.save()
        self.assertEqual(state.name, "California")

    @unittest.skipIf(db != "db", "test dbstorage only")
    def test_instance_dbstorage(self):
        """ """
        state1 = State(name="New_York")
        state1.save()
        self.assertNotEqual(state1.created_at, state1.updated_at)
        state2 = State(name="Texas")
        state2.save()
        self.assertNotEqual(state1.id, state2.id)
