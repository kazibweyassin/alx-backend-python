#!/usr/bin/env python3
"""
"""

from parameterized import parameterized
import unittest
from unittest.mock import patch
from unittest.mock import patch, Mock


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

# def get_json(url: str) -> Dict:
#     """Get JSON from remote URL.
#     """
#     response = requests.get(url)
#     return response.json()

class TestGetJson (unittest.TestCase):
    """Test json returns expected results"""
    @patch('utils.requesrs.get')
    def test_get_json(self, mock_get):

        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for test_url, test_payload in test_cases:

            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            mock_get.assert_called_once_with(test_url)

            mock_get.reset_mock()

class TestMemoize (unittest.TestCase):
    """momoize"""
    class TestClass:
        def a_method(self):
            return 42
        

    @memoize
    def a_property(self):
        return self.a_method()
    with patch.object(
        TestClass,
        "a_method",
        return_value=lambda:42,
    ) as memo_fcn:
        test_class = TestClass()
        self.assertEqual(test_class.a_method(), 42)
        self.assertEqual(test_class.a_propery(), 42)
        memo.assert_called_once()







if __name__ == "__main__":
    unittest.main()


            