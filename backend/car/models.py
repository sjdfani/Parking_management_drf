from django.db import models


class Car(models.Model):
    car_model = models.CharField(max_length=250)
    registration_code = models.CharField(max_length=250)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.car_model
