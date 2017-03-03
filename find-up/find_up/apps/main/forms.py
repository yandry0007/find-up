from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import Perfiles

class RegistrarseForm(forms.ModelForm):
	class Meta:
		model = Perfiles