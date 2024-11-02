#!/usr/bin/env python3
"""
"""

from parameterized import parameterized
import unittest
from unittest.mock import patch


from utils import (
    access_nested_map,
    get_json,
    memoize
)

class TestAccessNestedMap (unittest.TestCase):
    """Test access_nested_map utilis methods"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def TestAccessNestedMap(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
            self.assertEqual(f"KeyError('{expected}')", repr(err.exception))
            


