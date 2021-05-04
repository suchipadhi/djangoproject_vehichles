from django.urls import path

from .views import VehicleRegistrationView, VehicleDeleteView, VehicleLocationUpdateView

urlpatterns = [
    path("", VehicleRegistrationView.as_view(), name='vehicle-registration'),
    path("<uuid:pk>/locations/", VehicleLocationUpdateView.as_view(), name='location-update'),
    path("<uuid:pk>/", VehicleDeleteView.as_view(), name='vehicle-delete'),

]
