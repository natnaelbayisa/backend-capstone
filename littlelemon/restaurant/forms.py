from django.forms import ModelForm
from .models import Booking
from .models import NewUser


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class RegistrationForm(ModelForm):
    class Meta:
        model = NewUser
        fields = "__all__"