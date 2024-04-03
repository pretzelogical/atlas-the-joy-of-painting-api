import unittest
from db import TJOPDatabase


class TestTJOPDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.db = TJOPDatabase()

    def test_build_query_match_all(self):
        built_query = self.db.build_get_query_str({
            "match": "all",
            "month": ["1983-02", "1983-03"],
            "colors": ["Prussian Blue", "Sap Green", "Titanium White"],
            "subject": ["Mountain", "Trees"]
        })

        print(built_query, "\n")

    def test_build_query_match_all_colors(self):
        built_query = self.db.build_get_query_str({
            "match": "all",
            "month": ["1983-02"],
            "colors": ["Prussian Blue", "Sap Green", "Titanium White"],
        })

        print(built_query, "\n")

        built_query = self.db.build_get_query_str({
            "match": "all",
            "colors": ["Prussian Blue", "Sap Green", "Titanium White"],
        })

        print(built_query, "\n")

    def test_build_query_match_all_subject(self):
        built_query = self.db.build_get_query_str({
            "match": "all",
            "month": ["1983-02"],
            "subject": ["Mountain", "Trees"]
        })

        print(built_query, "\n")

    def test_build_query_match_all_month(self):
        built_query = self.db.build_get_query_str({
            "match": "all",
            "month": ["1983-02"]
        })
        print(built_query, "\n")

    def test_build_query_match_some(self):
        built_query = self.db.build_get_query_str({
            "match": "some",
            "month": ["1983-02", "1983-03"],
            "colors": ["Prussian Blue", "Sap Green", "Titanium White"],
            "subject": ["Mountain", "Grass", "Trees"]
        })

        print(built_query, "\n")

    def test_build_query_match_some_colors(self):
        built_query = self.db.build_get_query_str({
            "match": "some",
            "month": ["1983-02"],
            "colors": ["Prussian Blue", "Sap Green", "Titanium White"]
        })

        print(built_query, "\n")

    def test_build_query_match_some_subject(self):
        built_query = self.db.build_get_query_str({
            "match": "some",
            "month": ["1983-02"],
            "subject": ["Mountain", "Grass", "Trees"]
        })

        print(built_query, "\n")

    def test_build_query_match_some_month(self):
        built_query = self.db.build_get_query_str({
            "match": "some",
            "month": ["1990-07", "1983-02"],
        })

        print(built_query, "\n")
