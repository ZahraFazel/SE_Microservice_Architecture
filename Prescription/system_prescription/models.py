from django.db import models
from django.utils.timezone import datetime


class Prescription(models.Model):
    doctor_id = models.IntegerField()
    patient_id = models.IntegerField()
    drugs = models.TextField(max_length=2000)
    date = models.DateField(default=datetime.now)
