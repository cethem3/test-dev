from django.urls import path

from adventure import views

urlpatterns = [
    path("create-vehicle/", views.CreateVehicleAPIView.as_view()),
    path("create-service-area/", views.CreateServiceAreaAPIView.as_view()),
    path("vehicles/", views.GetVehiclesAPIView.as_view()),
    path("vehicle/<str:license_plate>/", views.GetVehicleAPIView.as_view()),
    path("start/", views.StartJourneyAPIView.as_view()),
]
