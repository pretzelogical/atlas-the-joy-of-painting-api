import unittest
from check_query import check_query
""" Test query validation """


class TestCheckQuery(unittest.TestCase):

    # TODO: Add tests for dates, match only fail, invalid keys
    def test_malformed_json(self):
        self.assertEqual(
            check_query(["match", "colors"]),
            "Malformed JSON"
        )

    def test_invalid_match(self):
        self.assertEqual(
            check_query({"match": "al", "colors": ["Black Gesso"]}),
            "Invalid match value al"
        )

    def test_invalid_colors(self):
        self.assertEqual(
            check_query({"match": "all", "colors": "Black Gesso"}),
            "Colors must be an array"
        )
        invalid_cols = ["Bright Red", "Black Gesso", "DROP ALL"]
        self.assertEqual(
            check_query({
                "match": "all",
                "colors": invalid_cols
            }),
            f"Invalid color in {invalid_cols}"
        )

    def test_invalid_subject(self):
        self.assertEqual(
            check_query({"match": "all", "subject": "Apple Frame"}),
            "Subject must be an array"
        )
        invalid_subj = ['Apple Frame', 'Conifer', 'Clouds?']
        self.assertEqual(
            check_query({
                "match": "all",
                "subject": invalid_subj
            }),
            f"Invalid subject in {invalid_subj}"
        )
