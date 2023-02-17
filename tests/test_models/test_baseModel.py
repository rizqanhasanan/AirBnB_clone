#!/usr/bin/python3
"""Module to test BaseModel class"""


from datetime import datetime, timedelta
import unittest
import io
from models.base_model import BaseModel
from contextlib import redirect_stdout
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

def setUp(self):
    """Set up which instance to call"""
    self._class = BaseModel()
    self._class2 = BaseModel()
    self._name = "BaseModel"

# -------------Tests Public Attributes-------------------------------

def test_idCorrect(self):
    """Test that id is a unique string"""
    my_model1 = self._class
    my_model2 = self._class2
    self.assertTrue((type(my_model1.id) is str))
    self.assertNotEqual(my_model1.id, my_model2.id)

def test_createUpdateType(self):
    """Test that create and update are datetime objects"""
    my_model = self._class
    self.assertTrue(isinstance(my_model.created_at, datetime))
    self.assertTrue(isinstance(my_model.updated_at, datetime))

