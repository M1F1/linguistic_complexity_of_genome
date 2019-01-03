import unittest
import distinct_substrings


class TestCreatingDistinctSubstringsFromString(unittest.TestCase):

    def test_create_substrings_idxs_1(self):
        result = distinct_substrings.create_substrings_idxs('a', 'alamakota')
        self.assertEqual(result, [(0, 1), (2, 3), (4, 5), (8, 9)])

    def test_create_substrings_idxs_2(self):
        result = distinct_substrings.create_substrings_idxs('kot', 'kotmkotpkot')
        self.assertEqual(result, [(0, 3), (4, 7), (8, 11)])

    def test_create_new_substrings(self):
        string = 'ala'
        result_idxs = distinct_substrings.create_substrings_idxs('a', string)
        self.assertEqual(result_idxs, [(0, 1), (2, 3)])
        result_new_idxs = distinct_substrings.create_new_substrings(result_idxs, string)
        self.assertEqual(result_new_idxs, [(0, 2)])

    def test_create_string_from_idxs(self):
        string = 'alamakota'
        start_idx, end_idx = 3, 5
        result = distinct_substrings.create_string_from_idxs(start_idx, end_idx, string)
        self.assertEqual(result, 'ma')

    def test_flatten_list(self):
        list_of_lists = [[1,2], [2,4]]
        result_list = distinct_substrings.flatten_list(list_of_lists)
        self.assertEqual(result_list, [1, 2, 2, 4])

    def test_create_all_distinct_substrings(self):
        string = "ATTTGGATT"
        result_substrings_len = len(distinct_substrings.create_all_distinct_substrings(string))
        self.assertEqual(result_substrings_len, 35)

    def test_create_all_distinct_substrings_2(self):
        string = "ala"
        result_substrings = distinct_substrings.create_all_distinct_substrings(string)
        self.assertEqual(result_substrings, {'a', 'al', 'la', 'ala', 'l'})



if __name__ == '__main__':
    unittest.main()