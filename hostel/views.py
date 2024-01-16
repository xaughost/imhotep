from django.shortcuts import render, get_object_or_404
from .models import Hostel, HostelImage, Room, Amenity, RoomImage

def index(request):
    hostel = Hostel.objects.first()
    images = HostelImage.objects.filter(hostel=hostel) if hostel else HostelImage.objects.none()
    rooms = Room.objects.all()
    amenity = Amenity.objects.filter(isFeatured=True).first()
    return render(request, 'index.html', {'hostel': hostel, 'images': images, 'rooms': rooms, 'amenity': amenity})

def about(request):
    hostel = Hostel.objects.first()
    images = HostelImage.objects.filter(hostel=hostel) if hostel else HostelImage.objects.none()
    return render(request, 'about.html', {'hostel': hostel, 'images': images})

def rooms(request):
    hostel = Hostel.objects.first()
    images = HostelImage.objects.filter(hostel=hostel) if hostel else HostelImage.objects.none()
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'hostel': hostel, 'images': images, 'rooms': rooms})

def room_details(request, item_id):
    room = get_object_or_404(Room, pk=item_id)
    images = RoomImage.objects.filter(room=room)
    return render(request, 'room_detail.html', {'room': room, 'images': images})

def facilities(request):
    hostel = Hostel.objects.first()
    images = HostelImage.objects.filter(hostel=hostel) if hostel else HostelImage.objects.none()
    amenities = Amenity.objects.all()
    return render(request, 'facilities.html', {'hostel': hostel, 'images': images, 'amenities': amenities})