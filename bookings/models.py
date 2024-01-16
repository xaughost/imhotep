from django.db import models
from hostel.models import Room

# Base Model for booking model
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Booking Model
class Booking(BaseModel):
    name = models.CharField(max_length=256)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guardian_name = models.CharField(max_length=256)
    student_id = models.CharField(max_length=8)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=10)
    guardian_mobile = models.CharField(max_length=10)
    student_id_image = models.ImageField(upload_to='student')
    payment_draft = models.ImageField(upload_to='payment')

    def __str__(self):
        return self.name
