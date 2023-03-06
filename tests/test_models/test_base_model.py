import unittest
from models.base_model import BaseModel
from datetime import datetime
import os.path
from models.engine.file_storage import FileStorage
import models


objects = FileStorage._FileStorage__objects


class testBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        first_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(first_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_str(self):
        model_str = str(self.model)
        self.assertIsInstance(model_str, str)
        self.assertIn('[BaseModel]', model_str)
        self.assertIn('id', model_str)
        self.assertIn(str(self.model.id), model_str)
        self.assertIn(str(self.model.__dict__), model_str)

    def test_save2(self):
        model = BaseModel()
        x = model.updated_at
        model.save()
        y = model.updated_at
        self.assertNotEqual(x, y)
        os.remove("file.json")

    def test_save_with_reload(self):
        self.assertEqual(os.path.isfile("file.json"), False)
        obj = FileStorage._FileStorage__objects.copy()
        model = BaseModel()
        model.save()
        self.assertNotEqual(obj, FileStorage._FileStorage__objects)
        self.assertEqual(os.path.isfile("file.json"), True)
        os.remove("file.json")
       

    if __name__ == '__main__':
        unittest.main()