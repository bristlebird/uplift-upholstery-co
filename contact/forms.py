"""
Form for sending message to store owner
"""
from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    """ Set up form for sending an enquiry """
    class Meta:
        model = Enquiry
        exclude = ('created-on',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, classes & update auto-generated labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your name',
            'email': 'Email Address',
            'message': 'Message',
            'phone_number': 'Phone Number',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
