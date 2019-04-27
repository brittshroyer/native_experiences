from rest_framework import viewsets, permissions

from app.models import Host, Traveler, Trip, Review
from .serializers import HostSerializer, TravelerSerializer, TripSerializer, ReviewSerializer

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HostSerializer

class TravelerViewSet(viewsets.ModelViewSet):
    queryset = Traveler.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TravelerSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TripSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReviewSerializer
