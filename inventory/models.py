from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Location(models.Model):
    location_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.location_name}"


class Consumable(models.Model):
    name = models.CharField(max_length=24, unique=True)
    item_location = models.ForeignKey(Location, on_delete=models.RESTRICT, related_name="stored")

    def __str__(self):
        return f"{self.name}"


class DateTable(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"{self.date}"


class Inventory(models.Model):
    item = models.ForeignKey(Consumable, on_delete=models.RESTRICT, related_name="item_name")
    count = models.IntegerField()
    date = models.ForeignKey(DateTable, on_delete=models.RESTRICT, related_name="date_recorded")
    counter = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="counter")

    def __str__(self):
        return f"{self.item}: {self.count}"
