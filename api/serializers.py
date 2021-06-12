"""
: This class is to serailize and deserailize the model instances
: to json representatives.
: It also define how the client app should make a request.
"""
from rest_framework import serializers
from api.models import User, Bike, Trip


class UserSerializer (serializers.ModelSerializer):
    """
        UserSerializer using ModelSerializer.
        The below is same as
        ```
            username = serializers.CharField (required=True)
            email = serializers.CharField (required=True)
            password = serializers.CharField (required=True)
        ```
        Create, Update methods will also be included by default in ModelSerializer,
        so that we don't need to create manually.
    """
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'password']


class BikeSerializer (serializers.Serializer):
    """
        Bike serializer
    """
    class Meta:
        model = Bike
        fields = ['bike_id', 'vendor', 'created_at']


class TripSerializer (serializers.ModelSerializer):
    """
        trip serializer
    """
    class Meta:
        model = Trip
        fields = ['trip_id', 'user', 'bike', 'start_time', 'duration']
