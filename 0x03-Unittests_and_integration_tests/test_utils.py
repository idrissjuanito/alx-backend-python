#!/usr/bin/env python3
""" Utils function test module """
from typing import Any, Mapping, Sequence
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ Test class for Acesss Nested maps """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any):
        """ Tests the access map method"""
        value = access_nested_map(nested_map, path)
        self.assertEqual(value, expected)
