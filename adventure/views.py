from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from adventure import models, notifiers, repositories, serializers, usecases


class CreateVehicleAPIView(APIView):
    def post(self, request: Request) -> Response:
        payload = request.data
        vehicle_type = models.VehicleType.objects.get(name=payload["vehicle_type"])
        vehicle = models.Vehicle.objects.create(
            name=payload["name"],
            passengers=payload["passengers"],
            vehicle_type=vehicle_type,
        )
        return Response(
            {
                "id": vehicle.id,
                "name": vehicle.name,
                "passengers": vehicle.passengers,
                "vehicle_type": vehicle.vehicle_type.name,
            },
            status=201,
        )

class CreateServiceAreaAPIView(APIView):
    def post(self, request: Request) -> Response:
        payload = request.data
        left_station = models.ServiceArea.objects.get(pk=payload["left_station"]) if "left_station" in payload else None
        right_station = models.ServiceArea.objects.get(pk=payload["right_station"]) if "right_station" in payload else None
        service_area = models.ServiceArea.objects.create(
            kilometer=payload["kilometer"],
            gas_price=payload["gas_price"],
            left_station=left_station,
            right_station=right_station
        )

        return Response(
            {
                "id": service_area.id,
                "kilometer": service_area.kilometer,
                "gas_price": service_area.gas_price,
                "left_station": service_area.left_station,
                "right_station": service_area.right_station
            },
            status=201
        )

class StartJourneyAPIView(generics.CreateAPIView):
    serializer_class = serializers.JourneySerializer

    def perform_create(self, serializer) -> None:
        repo = self.get_repository()
        notifier = notifiers.Notifier()
        usecase = usecases.StartJourney(repo, notifier).set_params(
            serializer.validated_data
        )
        try:
            usecase.execute()
        except usecases.StartJourney.CantStart as e:
            raise ValidationError({"detail": str(e)})

    def get_repository(self) -> repositories.JourneyRepository:
        return repositories.JourneyRepository()

class GetVehiclesAPIView(APIView):
    def get(self, request) -> Response:
        vehicles = models.Vehicle.objects.all()
        vehicles_serializer = serializers.VehicleSerializer(vehicles, many=True)
        return Response(
            vehicles_serializer.data,
            status=200
        )

class GetVehicleAPIView(APIView):
    def get(self, request, license_plate) -> Response:
        vehicles = models.Vehicle.objects.get(number_plate=license_plate)
        vehicles_serializer = serializers.VehicleSerializer(vehicles)
        return Response(
            vehicles_serializer.data,
            status=200
        )

class GetServiceAreaAPIView(APIView):
    def get(self, request, kilometer) -> Response:
        services = models.ServiceArea.objects.all()
        services_serializer = serializers.ServiceAreaSerializer(services, many=True)
        return Response(
            services_serializer.data, status=200
        )
class GetServiceAreaByKilometerAPIView(APIView):
    def get_by_kilometer(self, request, kilometer) -> Response:
        services = models.ServiceArea.objects.get(kilometer=kilometer)
        services_serializer = serializers.ServiceAreaSerializer(services, many=True)
        return Response(
            services_serializer, status=200
        )
    