from django.db import models

# Create your models here.

class Room(models.Model):
    rollno = models.CharField(max_length=10, default="0")
    room_no = models.CharField(max_length=6)
    name = models.CharField(max_length=101, default="0")
    is_alloted = models.BooleanField(default=False)
    block = models.CharField(max_length=1)
    floor = models.CharField(max_length=1, default="0")

    def __str__(self):
        return self.room_no
