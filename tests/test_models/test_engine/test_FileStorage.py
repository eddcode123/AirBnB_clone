#!/usr/bin/python3
""" Unittesting Filestorage class """
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_empty(self):
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{obj.id}", all_objects)

    def test_save_and_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn(f"BaseModel.{obj.id}", all_objects)

if __name__ == '__main__':
    unittest.main()
