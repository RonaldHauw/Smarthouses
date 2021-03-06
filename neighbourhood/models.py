from __future__ import unicode_literals
from django.db import models

from django.db import models

class Neighbourhood(models.Model):

    name = models.CharField(max_length=32)
    ref_id = models.CharField(max_length = 32)

    def __str__(self):
        return self.name

class House(models.Model):

    name = models.CharField(max_length=32)
    ref_id = models.CharField(max_length=32)

    neighbourhood = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.name


class Room(models.Model):

    #roomtypes = ((Kitchen,'Kitchen'),(Living_Room,'Living_Room'),(Hallway,'Hallway'),(Toilet,'Toilet'),(Laundry_Room,'Laundry_Room'),(Bedroom_1,'Bedroom_1'),(Bedroom_2,'Bedroom_2'),(Bathroom,'Bathroom'))

    house = models.ForeignKey(House)

    name = models.CharField(max_length=100)
    ref_id = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.name + '-' + self.house.name

####################################################################################################
#nummer pin en soort van een pin
####################################################################################################
class Smart_Devices(models.Model):

    name = models.CharField(max_length=100)
    ref_id = models.CharField(max_length=100)
    power = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=3,default=000)
    duration = models.CharField(max_length=100, default=0)
    deadline = models.CharField(max_length=100, default=0)
    status_function = models.CharField(max_length=100, default=0)
    optimal_status = models.CharField(max_length=100, default=0)


    description = models.TextField()
    room = models.ForeignKey(Room)
    house = models.ForeignKey(House)

    def __str__(self):
        return self.name + '-' + self.room.name



class Fridges(models.Model):

    name = models.CharField(max_length=100)
    ref_id = models.CharField(max_length=100)
    power = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=100, default=0)
    #duration = models.CharField(max_length=100, default=0)
    planned_status = models.CharField(max_length=100, default=0)
    optimal_status = models.CharField(max_length=100, default=0)

    description = models.TextField()
    room = models.ForeignKey(Room)

    def __str__(self):
        return self.name + '-' + self.room.name

####################################################################################################
####################################################################################################

class Heating(models.Model):

    name = models.CharField(max_length=100)
    ref_id = models.CharField(max_length=100)
    power = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=100, default=0)
    #duration = models.CharField(max_length=100, default=0)
    planned_status = models.CharField(max_length=100, default=0)
    optimal_status = models.CharField(max_length=100, default=0)

    description = models.TextField()
    room = models.ForeignKey(Room)

    def __str__(self):
        return self.name + '-' + self.room.name

####################################################################################################
####################################################################################################

class Battery(models.Model):

    name = models.CharField(max_length=100)
    ref_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default=0)
    power = models.CharField(max_length=100, default=0)
    #duration = models.CharField(max_length=100, default=0)
    planned_status = models.CharField(max_length=100, default=0)
    optimal_status = models.CharField(max_length=100, default=0)
    charged_status = models.CharField(max_length=100, default=0)

    description = models.TextField()
    room = models.ForeignKey(Room)

    def __str__(self):
        return self.name + '-' + self.room.name


class Stupid_Devices(models.Model):

    name = models.CharField(max_length=100)
    ref_id = models.CharField(max_length=100)
    power = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=100, default=0)

    description = models.TextField()
    room = models.ForeignKey(Room)

    def __str__(self):
        return self.name + '-' + self.room.name

#all status

class Optimal_Status_Smart_Devices(models.Model):

    name = models.ForeignKey(Fridges)
    hour = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=100, default=0)

class Plan_Status_Fridges(models.Model):

    name = models.ForeignKey(Fridges)
    hour = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=100, default=0)

class Plan_Status_Heating(models.Model):

    name = models.ForeignKey(Heating)
    hour = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=100, default=0)


class Plan_Status_Battery(models.Model):

    name = models.ForeignKey(Battery)
    hour = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=100, default=0)

class Plan_Status_Stupid_devices(models.Model):

    name = models.ForeignKey(Stupid_Devices)
    hour = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=100, default=0)

#optimal status

class Optimal_Status_Fridges(models.Model):

    name = models.ForeignKey(Fridges)
    hour = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=100, default=0)

class Optimal_Status_Heating(models.Model):

    name = models.ForeignKey(Fridges)
    hour = models.CharField(max_length=100, default=0)
    status = models.CharField(max_length=100, default=0)










####################################################################################################
####################################################################################################

####################################
#demo
####################################


########################################################################################################################
########################################################################################################################