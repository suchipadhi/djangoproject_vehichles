from rest_framework import serializers
from vehicles.models import Vehicles


class VehicleRegistrationSerializer(serializers.ModelSerializer):
    """
    The model serializer automatically generates a set of fields based on the model and also generates validators.
    They allow implementations such as .create() and .update().
    Here fields has exact fields as given in the model.
    """
    class Meta:
        model = Vehicles
        fields = ('id', 'vehicle_name', 'latitude', 'longitude', 'created_at', 'updated_at')
        read_only = ('id',)
