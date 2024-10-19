from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("Court 3,4", "Court 3,4"),
    ("Court 5,6", "Court 5,6"),
    ("Court 7,8", "Court 7,8"),
    ("Court 9,10", "Court 9,10"),
    ("Court 11,12", "Court 11,12"),
    ("Court 13,14", "Court 13,14"),
    ("Court 15,16", "Court 15,16"),
    ("Court 17,18", "Court 17,18"),
    ("Court 19,20", "Court 19,20"),
    ("Court 21,22", "Court 21,22"),
    ("Court 23,24", "Court 23,24"),
    ("Court 25,26", "Court 25,26"),
    ("Court 27,28", "Court 27,28"),
    ("Court 29,30", "Court 29,30"),
    ("Court 31,32", "Court 31,32"),
    ("Court 33,34", "Court 33,34"),
    )
TIME_CHOICES = (
    ("16.00 - 17.00", "16.00 - 17.00"),
    ("17.00 - 18.00", "17.00 - 18.00"),
    ("18.00 - 19.00", "18.00 - 19.00"),
    ("19.00 - 20.00", "19.00 - 20.00"),
    ("20.00 - 21.00", "20.00 - 21.00"),
    ("21.00 - 22.00", "21.00 - 22.00"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Court 3,4")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=30, choices=TIME_CHOICES, default="16.00 - 17.00")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"