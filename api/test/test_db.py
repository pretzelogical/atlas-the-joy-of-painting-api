import unittest
from db import TJOPDatabase


class TestTJOPDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.db = TJOPDatabase()

    def test_build_query_match_all(self):
        built_query = self.db.build_query({
            "match": "some",
            "month": "1983-02",
            "colors": ["Prussian Blue", "Sap Green", "Titanium White"],
            "subject": ["Mountain", "Grass", "Trees"]
        })

        print(built_query)