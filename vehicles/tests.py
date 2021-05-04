import uuid

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vehicles.models import Vehicles


class VehiclesTests(APITestCase):
    def setUp(self):
        self.post_url = reverse('vehicle-registration')
        self.post_data = {'id': uuid.uuid1()}
        self.update_data = {
            "latitude": 10.0,
            "longitude": 20.0
        }

    def test_register_vehicels_with_valid_uuid(self):
        """
        Test for registering the vehicle with a valid uuid. This test returns 204 after successful creation.
        """
        response = self.client.post(self.post_url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['vehicle_id'])
        response = self.client.post(self.post_url, self.post_data, format='json')
        self.assertEqual(response.data, {})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_register_vehicels_with_invalid_uuid(self):
        """
        Test for not registering the vehicle with an invalid id. This test returns 400.
        """
        data = {'id': 'invalid_uuiid'}
        response = self.client.post(self.post_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNotNone(response.data['detail_error'])

    def test_update_vehicels_with_valid_uuid(self):
        """
        Test for updating the vehicle details when provided with a valid id.
        Checks for the scenario "The vehicle will never contact this endpoint without having registered first."
        """
        response = self.client.post(self.post_url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['vehicle_id'])
        vehicle = Vehicles.objects.get(id=response.data['vehicle_id'])
        update_url = Vehicles.get_update_vehicle_url(vehicle)

        response = self.client.put(update_url, self.update_data, format='json')
        self.assertEqual(response.data, {})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        updated_vehicle = Vehicles.objects.get(id=vehicle.id)
        self.assertEqual(updated_vehicle.latitude, self.update_data['latitude'])
        self.assertEqual(updated_vehicle.longitude, self.update_data['longitude'])

    def test_update_vehicels_with_invalid_uuid(self):
        """
        Test for id before updating the vehicle details when provided with a invalid id.
        """
        Vehicles.objects.create(id=uuid.uuid1())
        update_url = reverse('location-update', kwargs={"pk": uuid.uuid1()})
        response = self.client.put(update_url, self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_vehicels_with_valid_uuid(self):
        """
        Test for deleting the vehicle details if id exists.
        """
        response = self.client.post(self.post_url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['vehicle_id'])
        vehicles = Vehicles.objects.filter(id=response.data['vehicle_id'])
        delete_url = Vehicles.get_delete_vehicle_url(vehicles.first())
        response = self.client.delete(delete_url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(vehicles), 0)

    def test_delete_vehicles_with_invalid_uuid(self):
        """
        Test for not deleting the vehicle details if id does not exists or provided with invalid id.
        """
        response = self.client.post(self.post_url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['vehicle_id'])
        vehicle = Vehicles.objects.filter(id=response.data['vehicle_id'])
        delete_url = reverse('vehicle-delete', kwargs={"pk": uuid.uuid1()})
        response = self.client.delete(delete_url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(vehicle), 1)
