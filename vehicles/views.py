# Create your views here.
import json
from uuid import UUID

from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from vehicles.models import Vehicles
from vehicles.serializers import VehicleRegistrationSerializer


class VehicleDeleteView(generics.DestroyAPIView):
    """
    Generics extends the APIView class making it easier to and quick to build API view similar to the database models.
    Used for delete-only endpoints for a single model instance. This provides delete method handler.
    """
    def get_serializer_class(self):
        """

        :return: VehicleRegistrationSerializer
        """
        return VehicleRegistrationSerializer

    def destroy(self, request, *args, **kwargs):
        """

        :param request: DELETE
        :param args:
        :param kwargs:vehicle_id
        :return:
        """
        try:
            vehicle_id = self.kwargs.get('pk', None)
            vehicle = get_object_or_404(Vehicles.objects.all(), id=vehicle_id)
            self.perform_destroy(vehicle)
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Http404 as ht:
            return Response({'detail_message': json.dumps(vars(ht))}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail_error': e}, status=status.HTTP_400_BAD_REQUEST)


class VehicleRegistrationView(generics.CreateAPIView):
    """
    CreateAPIView is Used for create-only endpoints . This provides post method handler.
    """

    def get_queryset(self):
        """

        :return: vehicle objects
        """
        vehicle_id = self.request.data
        return Vehicles.objects.filter(id=vehicle_id)

    def get_serializer_class(self):
        """

        :return:VehicleRegistrationSerializer
        """
        return VehicleRegistrationSerializer

    def create(self, request, *args, **kwargs):
        """

        :param request: POST
        :param args:
        :param kwargs:
        :return: vehicle object
        """
        try:
            vehicle_id = self.request.data.get('id', None)
            vehicle = Vehicles.objects.filter(id=vehicle_id)
            if not vehicle:
                Vehicles.objects.create(id=vehicle_id)
                return Response({'vehicle_id': vehicle.first().id}, status=status.HTTP_201_CREATED)
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'detail_error': e}, status=status.HTTP_400_BAD_REQUEST)


class VehicleLocationUpdateView(generics.UpdateAPIView):
    """
    UpdateAPIView is Used for update-only endpoints for a single model instance.
    This provides both put and patch method handler.
    """

    def get_serializer_class(self):
        """

        :return:VehicleRegistrationSerializer
        """
        return VehicleRegistrationSerializer

    def update(self, request, *args, **kwargs):
        """

        :param request: PUT
        :param args:
        :param kwargs:vehicle id
        :return:
        """
        try:
            vehicle_id = self.kwargs.get('pk', None)
            latitude = self.request.data.get('latitude', None)
            longitude = self.request.data.get('longitude', None)
            vehicle = get_object_or_404(Vehicles.objects.all(), id=vehicle_id)
            vehicle.latitude = latitude
            vehicle.longitude = longitude
            vehicle.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Http404 as ht:
            return Response({'detail_message': json.dumps(vars(ht))}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail_error': e}, status=status.HTTP_400_BAD_REQUEST)
