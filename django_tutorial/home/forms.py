from django import forms
from . models import Booking,Contacts
class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        widgets={
            'booking_date':DateInput()
        }
        labels={
            'p_phone':'Patient Phone:',
            'p_name':'Patient Name:',
            'p_email':'Patient Email',
            'doc_name':'Doctor Name',
            'booking_date':'Booking Date',
              
        }
class ContactsForm(forms.ModelForm):
    class Meta:
        model=Contacts
        fields='__all__'
        labels={
            'p_phone':'Patient Phone:',
            'p_name':'Patient Name:',
            'p_email':'Patient Email',
           'message':'Message'
              
        }