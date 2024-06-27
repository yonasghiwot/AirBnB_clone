#!/usr/bin/python3
"""Unittest for Amenity"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_init(self):
         """Test default initialization of Amenity"""
        snapshot = datetime.now()
        amenity1 = Amenity()
        snapshot2 = datetime.now()

        self.assertIsInstance(amenity1.id, str)
        self.assertTrue(len(amenity1.id) > 0)
        self.assertTrue('Amenity.' + amenity1.id in storage.all().keys())

        self.assertIsInstance(amenity1.created_at, datetime)
        self.assertLess(amenity1.created_at, snapshot2)
        self.assertGreater(amenity1.created_at, snapshot)
        self.assertIsInstance(amenity1.updated_at, datetime)
        self.assertLess(amenity1.updated_at, snapshot2)
        self.assertGreater(amenity1.updated_at, snapshot)
        amenity1.save()
        self.assertIsInstance(amenity1.updated_at, datetime)
        self.assertGreater(amenity1.updated_at, snapshot)
        self.assertGreater(amenity1.updated_at, snapshot2)
        del amenity1

    def test_init_dict(self):
        """Test initialization of Amenity with a dictionary"""
        test_dict = {'updated_at': datetime(1973, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbg-27de-630706f8313c', 'created_at': datetime(1973, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        amenity2 = Amenity(**test_dict)

        self.assertIsInstance(amenity2.id, str)
        self.assertTrue(len(amenity2.id) > 0)
        self.assertTrue(amenity2.id == test_dict['id'])

        self.assertIsInstance(amenity2.created_at, datetime)
        self.assertTrue(amenity2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(amenity2.updated_at, datetime)
        self.assertTrue(amenity2.updated_at.isoformat('T') == test_dict['updated_at'])
        am2.save()
        self.assertGreater(amenity2.updated_at, amenity2.created_at)
        del amenity2

    def test_attribute(self):
        """Test attributes of Amenity"""
        amenity3 = Amenity()

        self.assertTrue(hasattr(amenity3, "name"))
        self.assertIsInstance(amenity3.name, str)
