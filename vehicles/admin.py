from django.contrib import admin

from .models import Vehicles


class VehiclesAdmin(admin.ModelAdmin):
    """
    Admin interface is created with metadata from the models, thus provides a model centric interface to teh user.
    Create a user to login with: "django-admin createsuperuser".
    """
    list_display = ('id', 'vehicle_name', 'latitude', 'longitude', 'created_at',
                    'updated_at')
    search_fields = ['vehicle_name', ]


admin.site.register(Vehicles, VehiclesAdmin)
