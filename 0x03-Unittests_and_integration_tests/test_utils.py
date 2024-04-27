#!/usr/bin/env python3
""" Utils function test module """
from typing import Any, Mapping, Sequence
from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from parameterized import parameterized
from requests import utils
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Test class for Acesss Nested maps """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Any):
        """ Tests the access map method """
        value = access_nested_map(nested_map, path)
        self.assertEqual(value, expected)

    @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence):
        """ Tests the access map function with raising errors """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """ Test for get_json function """
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, mock_requests):
        """ Test for return value of get json """
        mock_json = Mock()
        mock_json.json.return_value = test_payload
        mock_get = Mock()
        mock_get.return_value = mock_json
        mock_requests.get = mock_get

        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once()


class TestMemoize(TestCase):
    """ Memoize function tests """
    def test_memoize(self):
        """ Test correct values for memoize """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            new_test = TestClass()
            result = new_test.a_property
            result_2 = new_test.a_property
            self.assertEqual(result, 42)
            mock_method.assert_called_once()
