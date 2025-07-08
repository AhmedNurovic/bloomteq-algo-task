import unittest
from lookup import lookup

class TestLookup(unittest.TestCase):
    def test_valid_path_depth_2(self):
        obj = {"a": {"b": 1}}
        self.assertEqual(lookup(obj, "a.b"), 1)

    def test_valid_path_depth_1(self):
        obj = {"a": 1}
        self.assertEqual(lookup(obj, "a"), 1)

    def test_missing_top_level_key(self):
        obj = {"a": {"b": 1}}
        self.assertIsNone(lookup(obj, "c"))

    def test_missing_nested_key(self):
        obj = {"a": {"b": 1}}
        self.assertIsNone(lookup(obj, "a.c"))

    def test_non_dict_intermediate_value(self):
        obj = {"a": {"b": 1}}
        self.assertIsNone(lookup(obj, "a.b.c"))

    def test_empty_path(self):
        obj = {"a": {"b": 1}}
        self.assertEqual(lookup(obj, ""), obj)

    def test_path_with_empty_keys(self):
        obj = {"a": {"": 2}}
        self.assertEqual(lookup(obj, "a."), 2)

    def test_path_starting_with_empty_key(self):
        obj = {"": {"b": 3}}
        self.assertEqual(lookup(obj, ".b"), 3)

    def test_consecutive_dots(self):
        obj = {"a": {"": {"b": 4}}}
        self.assertEqual(lookup(obj, "a..b"), 4)

if __name__ == "__main__":
    unittest.main() 