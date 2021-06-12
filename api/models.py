from django.db import models
from datetime import datetime

class User (models.Model):
    """
    User Model
    """

    user_id = models.CharField (max_length=100, blank=True, primary_key=True)
    username = models.CharField (max_length=32, blank=False)
    email = models.CharField (max_length=100, blank=False)
    password = models.CharField (max_length=100, blank=False)
    created_at = models.DateTimeField (auto_now_add=True)

    def __str__ (self):
        return "id: %s, name: %s" % (self.user_id, self.username)

    class Meta:
        # by default, order the user lists by created_at value
        ordering = ['created_at']


class Bike (models.Model):
    """
    Bike Model
    """
    bike_id = models.CharField (max_length=100, blank=True, primary_key=True)
    vendor = models.CharField (max_length=100, blank=False)
    created_at = models.DateTimeField (auto_now_add=True)

    class Meta:
        ordering = ['created_at']


class Trip (models.Model):
    """
    Trip Model
    """
    trip_id = models.CharField (max_length=100, blank=True, primary_key=True)
    user = models.ForeignKey (User, on_delete=User)
    bike = models.ForeignKey (Bike, on_delete=Bike)
    start_time = models.CharField (max_length=100, default=datetime.now().strftime('%Y%m%d%H%M%s'))
    duration = models.IntegerField (default=0, blank=False)
