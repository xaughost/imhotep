from django.db import models

# Create hostel model
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create hostel model
class Hostel(BaseModel):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    message = models.TextField()
    phone = models.CharField(null=True, blank=True, max_length=25)
    email = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=256)
    isAvailable = models.BooleanField(default=True)
    minPrice = models.DecimalField(max_digits=10, decimal_places=2)
    maxPrice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class HostelImage(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hostel')
    isFeatured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.hostel.name} Located At {self.hostel.location}'

# hostel rooms
class Room(BaseModel):
    hostelItem = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    isAvailable = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rooms')

    def __str__(self):
        return f'{self.room.name}'

# hostel rooms
class Amenity(BaseModel):
    hostelItem = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    isFeatured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class AmenityImage(models.Model):
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='amenities')

    def __str__(self):
        return f'{self.amenity.name}'