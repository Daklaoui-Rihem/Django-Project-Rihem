from django import forms
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md'}),
        }
