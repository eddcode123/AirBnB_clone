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
        # check type of each instance attribute
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.update_at, datetime)

    def test_initialization_without_arguments(self):
        # Verify that 'id' is a valid UUID string
        self.assertTrue(self.base_model.id)
        # Verify that 'created_at' is a datetime object
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_id(self):
        # check if unique ids are assigned everytime to an object when its created
        obj_1 = self.base_model
        obj_2 = self.base_model
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_save_method(self):
        # check if update_date changes when save method is called to the time save() is called
        initial_time = self.base_model.update_at
        self.base_model.save()
        self.assertNotEqual(initial_time, self.base_model.updated_at)

    def test_string_rep(self):
        # check if the method returns a string representation of the BaseModel class
        result = f'{['BaseModel']} {(self.base_model.id)} {self.base_mode.__dict__}'
        self.assertEqual(str(self.base_model), result)

    def test_string_to_datetime_conversion(self):
        # cheking if the string has been converted to a datetime object
        obj_dict = {'created_at': '2022-02-21T12:00:00.000000', 'updated_at': '2022-02-21T12:00:00.000000'}
        recreated = BaseModel(**obj_dict)
        self.assertIsInstance(recreated.created_at, datetime)
        self.assertIsInstance(recreated.updated_at, datetime)

    def test_to_dict(self):
        # check if to dict method returns a dictionary object
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__name__'], 'BaseModel')
        self.assertIs(obj_dict['created_at'], str)
        self.assertIs(obj_dict['updated_at'], str)

    def recreate_instance_from_dic(self):
        # Verify that the recreated instance has the correct attributes and values
        obj_dict = self.base_model.to_dict()
        recreated_instance = BaseModel(**obj_dict)
        self.assertEqual(recreated_instance.id, self.base_model.id)
        self.assertEqual(recreated_instance.created_at, self.base_model.created_at)
        self.assertEqual(recreated_instance.update_at, self.base_model.update_at)

    def test_attribute_access(self):
        self.base_model.some_attribute = 'some_value'
        self.assertEqual(self.base_model.some_attribute, 'some_value')


if __name__ == '__main__':
    unittest.main()
