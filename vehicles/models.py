from django.db import models
import uuid

# Create your models here.
from django.urls import reverse


class Vehicles(models.Model):
    """
    Model is created with explicit validation parameters such as unique validator and certain validation
    logic is mentioned for latitude and longitudes as well.
    Two datetime fields are stored with creation and updation date.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_name = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, null=True, blank=True)
    longitude = models.DecimalField(default=0.0, max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """
        :return: unicode (text)
        """
        return self.id

    def get_update_vehicle_url(self):
        """
        Update and return a new instance, given the validated data.
        :return:
        """
        return reverse('location-update', kwargs={"pk": self.pk})

    def get_delete_vehicle_url(self):
        """
        Delete and return a new instance, given the validated data.
        :return:
        """
        return reverse('vehicle-delete', kwargs={"pk": self.pk})
