from django.test import TestCase, Client

from models import CatModel


class CatModelTest(TestCase):

    def setUp(self):
        self.cat_a = CatModel(
            name="A",
            length=10,
            width=20,
            height=30
        )
        self.cat_a.save()

    def test_get_volume(self):
        """
        Compare cat_a volume with known value
        """
        self.assertEqual(self.cat_a.volume(), 6000)


class CatApiTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_and_get_cat(self):
        response = self.client.post(
                "/api/cat/",
                data={
                    "name":"API cat",
                    "length": 10,
                    "width": 20,
                    "height": 30
                })
        self.assertEqual(response.status_code, 201)

        response = self.client.get("/api/cat/1/")

        self.assertEqual(
                response.content,
                """{"name":"API cat","length":10,"height":30,"width":20,"volume":6000}"""
        )
        self.assertEqual(response.status_code, 200)
