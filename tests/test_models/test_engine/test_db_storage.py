#!/usr/bin/python3
"""Unittest for DBStorage"""

import os
from models import *
import MySQLdb
from models.engine.db_storage import DBStorage
import unittest


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "Test DBStorage")
class TestDbstorage(unittest.TestCase):
    """unittest for DBStorage"""
    count1 = 0

    @classmethod
    def setUp(cls):
        """starting mysql connector"""
        cls.db = MySQLdb.connect(host="localhost", user="hbnb_test",
                                 passwd="hbnb_test_pwd", db="hbnb_test_db")
        cls.cursor = cls.db.cursor()

    @classmethod
    def tearDown(cls):
        """close the MySql connection"""
        cls.cursor.close()
        cls.db.close()

    def test_env(self):
        """Test Env"""
        self.assertEqual(os.getenv("HBNB_ENV"), "test")

    def test_all(self):
        """Testing method all"""
        state = State(name="California")
        storage.new(state)
        state.save()
        all_states = storage.all()
        self.assertTrue(isinstance(all_states, dict))

    def test_new(self):
        """test new method"""
        user = User(email="ji@naij.com", password="jipwd")
        storage.new(user)
        user.save()
        self.assertEqual(user.password, "jipwd")

    def test_save(self):
        """test delete method"""
        state = State(name="Texas")
        storage.new(state)
        state.save()
        query = f"SELECT COUNT(*) FROM states;"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.count1 = result[0]

    def test_delete(self):
        state1 = State(name="New York")
        storage.new(state1)
        state1.save()
        storage.delete(state1)
        query = f"SELECT COUNT(*) FROM states;"
        self.cursor.execute(query)
        result1 = self.cursor.fetchone()
        count2 = result1[0]
        self.assertNotEqual(count2, self.count1)
