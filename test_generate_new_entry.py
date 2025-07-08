import unittest
from generate_new_entry import generate_new_entry

class TestGenerateNewEntry(unittest.TestCase):
    def test_example_input(self):
        data = [
            {"id": 1, "value": 3},
            {"id": 2, "value": 7},
            {"id": 3, "value": 3},
            {"id": 4, "value": 1},
            {"id": 5, "value": 4},
        ]
        self.assertEqual(generate_new_entry(data), {"id": 6, "value": 5})

    def test_empty_list(self):
        self.assertIsNone(generate_new_entry([]))

    def test_no_duplicates(self):
        self.assertIsNone(generate_new_entry([{"id": 1, "value": 1}]))

    def test_duplicates_candidate_skipped(self):
        data = [
            {"id": 1, "value": 1},
            {"id": 2, "value": 1},
        ]
        # value=2 is the smallest not present, min_duplicate=1 < 2, so value=2 is valid
        self.assertEqual(generate_new_entry(data), {"id": 3, "value": 2})

    def test_gap_in_values(self):
        data = [
            {"id": 1, "value": 2},
            {"id": 2, "value": 2},
        ]
        # value=1 is not present, but min_duplicate=2 < 1 is False, so skip 1
        # next candidate is 3, min_duplicate=2 < 3 is True, so value=3
        self.assertEqual(generate_new_entry(data), {"id": 3, "value": 3})

    def test_ids_not_consecutive(self):
        data = [
            {"id": 10, "value": 5},
            {"id": 11, "value": 5},
        ]
        # new_id should be 12
        self.assertEqual(generate_new_entry(data), {"id": 12, "value": 6})

    def test_large_dataset(self):
        # 1000 entries, values 1-500 each appear twice
        data = []
        for i in range(1, 501):
            data.append({"id": i, "value": i})
            data.append({"id": i+500, "value": i})
        # All values 1-500 appear twice, so min_duplicate=1
        # Candidates: 501 (since 1-500 are present)
        self.assertEqual(generate_new_entry(data), {"id": 1001, "value": 501})

if __name__ == "__main__":
    unittest.main() 