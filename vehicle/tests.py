from rest_framework import status
from rest_framework.test import APITestCase

from vehicle.models import Car


# Create your tests here.
class VehicleTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_car(self):
        """Тестирование создания машин"""
        data = {
            'title': 'Test',
            'description': 'Test'
        }
        response = self.client.post(
            '/cars/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'milage': [], 'title': 'Test', 'description': 'Test', 'owner': None}
        )

        self.assertTrue(
            Car.objects.all().exists()
        )

