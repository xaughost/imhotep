from django.contrib import admin
from .models import Hostel, Room, HostelImage, RoomImage, Amenity, AmenityImage

# Merging the hostel and hostelImage model.
class HostelImageInline(admin.StackedInline):
    model = HostelImage
    extra = 1

class HostelAdmin(admin.ModelAdmin):
    inlines = [HostelImageInline]


# Merging the Room and RoomImage models.
class RoomImageInline(admin.StackedInline):
    model = RoomImage
    extra = 1
    
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]

# Merging the Amenities and Amenities Image models.
class AmenityImageInline(admin.StackedInline):
    model = AmenityImage
    extra = 1
    
class AmenityAdmin(admin.ModelAdmin):
    inlines = [AmenityImageInline]



# Register your models here.
admin.site.register(Hostel, HostelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Amenity, AmenityAdmin)
