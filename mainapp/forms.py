from django import forms
from .models import UserRegistration, ListingAppliances

class UserForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'

class ListForm(forms.ModelForm):
    class Meta:
        model = ListingAppliances
        fields = '__all__'
        exclude = ('email_id','view_count','property_id')