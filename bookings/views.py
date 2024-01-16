from django.shortcuts import render, redirect
from .forms import BookingForm

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # You can add additional logic or redirection here after successful form submission
            return redirect('/')  # Change 'success_page' to the actual URL or name

    else:
        form = BookingForm()

    return render(request, 'create_booking.html', {'form': form})

