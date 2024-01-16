# yourapp/forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mb-4 p-2 border text-sm w-full'}),
            'guardian_name': forms.TextInput(attrs={'class': 'mb-4 p-2 border text-sm w-full'}),
            'student_id': forms.TextInput(attrs={'class': 'mb-4 p-2 border text-sm w-full'}),
            'email': forms.EmailInput(attrs={'class': 'mb-4 p-2 border text-sm w-full'}),
            'mobile': forms.TextInput(attrs={'class': 'mb-4 p-2 border text-sm w-full'}),
            'guardian_mobile': forms.TextInput(attrs={'class': 'mb-4 p-2 border text-sm w-full'}),
            'room': forms.Select(attrs={'class': 'mb-4 p-2 border text-sm w-full'}),
            'student_id_image': forms.ClearableFileInput(attrs={'class': 'mb-4'}),
            'payment_draft': forms.ClearableFileInput(attrs={'class': 'mb-4'}),
        }
