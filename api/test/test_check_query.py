import unittest
from check_query import check_query
""" Test query validation """


class TestCheckQuery(unittest.TestCase):

    def test_empty_object(self):
        self.assertEqual(check_query({}), None)

    def test_match(self):
        self.assertEqual(
            check_query({"match": "all", "colors": ["Black Gesso"]}),
            None
        )
        self.assertEqual(
            check_query({"match": "some", "subject": ["Apple Frame"]}),
            None
        )

    def test_colors(self):
        self.assertEqual(
            check_query({
                "match": "all",
                "colors": ['Liquid Black', 'Liquid Clear',
                           'Midnight Black', 'Phthalo Blue']
                }),
            None
        )

    def test_month(self):
        self.assertEqual(
            check_query({
                "match": "all",
                "month": ["1983-01"]
                }),
            None
        )

    def test_subject(self):
        self.assertEqual(
            check_query({
                "match": "some",
                "subject": ['Diane Andre', 'Dock',
                            'Double Oval Frame', 'Farm']
            }),
            None
        )

    def test_fields(self):
        self.assertEqual(
            check_query({
                "match": "all",
                "fields": ["name", "youtube_src"],
                "subject": ["Dock"]
            }),
            None
        )

    # Test failures

    def test_malformed_json(self):
        self.assertEqual(
            check_query(["match", "colors"]),
            "Malformed JSON"
        )

    def test_invalid_keys(self):
        self.assertEqual(
            check_query({
                "match": "some",
                "month": ["1983-02"],
                "colors": ["Black Gesso"],
                "subjet": ["Apple Frame"]
            }),
            "Invalid key subjet in ['match', 'month', 'colors', 'subjet']"
        )
        self.assertEqual(
            check_query({
                "match": "some",
                "month": ["1983-02"],
                "colors": ["Black Gesso"],
                "subject": ["Apple Frame"],
                "monkey": "wrench"
            }),
            ("Invalid key monkey in "
             "['match', 'month', 'colors', 'subject', 'monkey']")
        )

    def test_invalid_month_format(self):
        self.assertEqual(
            check_query({
                "match": "some",
                "month": ["1983-2-1"]
            }),
            'Invalid date 1983-2-1 format must be YYYY-MM in [\'1983-2-1\']'
        )

    def test_month_out_of_range(self):
        self.assertEqual(
            check_query({
                "match": "some",
                "month": ["1982-12"]
            }),
            'Date 1982-12 out of range in [\'1982-12\']'
        )
        self.assertEqual(
            check_query({
                "match": "some",
                "month": ["1994-06"]
            }),
            'Date 1994-06 out of range in [\'1994-06\']'
        )

    def test_match_only_fail(self):
        query = {"match": "all"}
        self.assertEqual(
            check_query(query),
            (f"Query {query} requires month, colors and subject to be a non "
                "empty array")
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
            f"Invalid color DROP ALL in {invalid_cols}"
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
            f"Invalid subject Clouds? in {invalid_subj}"
        )

    def test_empty_fields(self):
        query = {
                "match": "all",
                "colors": [],
                "subject": []
        }
        self.assertEqual(
            check_query(query),
            None
        )
