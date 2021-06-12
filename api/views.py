"""
: API View class
: This class has the required to response for coresponding api end points.
"""
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

import uuid

from api.models import User, Bike, Trip
from api.serializers import UserSerializer, BikeSerializer, TripSerializer


class UserList (APIView):
    """
    GET Request -> List all the users
    POST Request -> Create new user
    """
    def get (self, request, format=None):
        # the reason of format=None is to handle any requests with explicit format, for eg. url/users.json
        # list all users and response
        print ("### DEBUG ### request", type (request))
        users = User.objects.all()
        serializer = UserSerializer (users, many=True)
        return JsonResponse (serializer.data, safe=False)

    def post (self, request, format=None):
        # create new user
        data = JSONParser().parse(request)
        data['user_id'] = str(uuid.uuid1()) # generating user_id
        serializer = UserSerializer (data=data)
        if (serializer.is_valid()):
            serializer.save() # create and save the new user
            return JsonResponse (serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail (APIView):
    """
    Get, Update, Delete a single user by user_id.
    """
    def get_user (self, user_id):
        try:
            return User.objects.get (user_id=user_id) # get existing user by user_id
        except User.DoesNotExist:
            return HttpResponse (status=status.HTTP_404_NOT_FOUND)

    def get (self, request, user_id, format=None):
        # return user details
        user = self.get_user (user_id)
        serializer = UserSerializer (user)
        return JsonResponse (serializer.data)

    def put (self, request, user_id, format=None):
        # update/edit user
        data = JSONParser().parse(request)
        user = self.get_user (user_id)
        serializer = UserSerializer (user, data = data)
        if serailizer.is_valid():
            serializer.save()
            return JsonResponse (serializer.data)
        return JsonResponse (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, user_id, format=None):
        # delete user
        user = self.get_user (user_id)
        user.delete()
        return HttpResponse (status=status.HTTP_204_NO_CONTENT)


class BikeList (APIView):
    """
    Get all bikes or Create a new bike
    """

    def get (self, request, format=None):
        # list all the bikes
        bikes = Bike.objects.all()
        serializer = BikeSerializer (bikes, many=True)
        return JsonResponse (serializer.data, safe=False)

    def post (self, request):
        # create a new bike
        data = JSONParser().parse (request)
        data['bike_id'] = str (uuid.uuid1())
        serializer = BikeSerializer (data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse (serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BikeDetail (APIView):
    """
    Get/ Update/ Delete single bike detail by bike_id
    """

    def get_bike (self, bike_id):
        # get bike by bike_id
        try:
            return Bike.objects.get (bike_id=bike_id)
        except Bike.DoesNotExist:
            return HttpResponse (status=status.HTTP_404_NOT_FOUND)

    def get (self, request, bike_id, format=None):
        # get single bike detail
        bike = self.get_bike (bike_id)
        serializer = BikeSerializer (bike)
        return JsonResponse (serializer.data)

    def put (self, request, bike_id, format=None):
        # update/edit bike detail
        data = JSONParser().parse (request)
        bike = self.get_bike (bike_id)
        serializer = BikeSerializer (bike, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse (serializer.data)
        return JsonResponse (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, bike_id):
        # delete/remove bike from database
        bike = self.get_bike (bike_id)
        bike.delete()
        return HttpResponse (status=status.HTTP_204_NO_CONTENT)


class TripList (APIView):
    """
    Get all the trips or create new trip
    """

    def get (self, request, format=None):
        trips = Trip.objects.all ()
        serializer = TripSerializer (trips, many=True)
        return JsonResponse (serializer.data, safe=False)

    def post (self, request):
        data = JSONParser().parse(request)
        print ("### DEBUG ### Creating new trip", data)
        # check whether the request is valid
        if 'user_id' not in data or 'bike_id' not in data:
            print ("invalid data!!")
            return HttpResponse (status=status.HTTP_400_BAD_REQUEST)
        return "Good to go!"


class UserTrip (APIView):
    """
    Get trips by user_id
    """
    def get (self, request, user_id, format=None):
        try:
            user = User.objects.filter (user_id=user_id)
            trip = Trip.objects.get (user=user)
        except User.DoesNotExist:
            print ("ERROR!!! User Not Found!!")
            return HttpResponse (status=status.HTTP_404_NOT_FOUND)
        except Trip.DoesNotExist:
            print ("ERROR!!! Trip Not Found!!")
            return HttpResponse (status=status.HTTP_404_NOT_FOUND)
