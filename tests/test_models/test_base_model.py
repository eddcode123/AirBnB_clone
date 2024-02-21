#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
    TestBaseModel__str__
"""
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModle(unittest.TestCase):
    """ define a class that test our base model class """

    def setUp(self):
        base_model = self.BaseModel()

    def test_instantiation(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.update_at, datetime)

    def test_id(self):
        obj_1 = self.base_model
        obj_2 = self.base_model
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_save_method(self):
        initial_time = self.base_model.update_at
        self.base_model.save()
        self.assertNotEqual(initial_time, self.base_model.updated_at)

    def test_string_rep(self):
        result = f'{['BaseModel']} {(self.base_model.id)} {self.base_mode.__dict__}'
        self.assertEqual(str(self.base_model), result)

    def test_to_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__name__'], 'BaseModel')
        self.assertIs(obj_dict['created_at'], str)
        self.assertIs(obj_dict['updated_at'], str)

    def test_attribute_access(self):
        self.base_model.some_attribute = 'some_value'
        self.assertEqual(self.base_model.some_attribute, 'some_value')


if __name__ == '__main__':
    unittest.main()
