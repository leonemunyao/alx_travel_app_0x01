from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated


class ListingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing reviews.
    """
    queryset = Review.objects.all()
    serializer_class = BookingSerializer  # Assuming you have a ReviewSerializer defined
    permission_classes = [IsAuthenticated]
