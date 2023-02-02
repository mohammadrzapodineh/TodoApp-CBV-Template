from django import forms
from .models import Todo
from django.core.validators import MaxLengthValidator

class TodoCreateForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title',)
        validators = {
            'title': MaxLengthValidator(110, message='Title Max Lenght= 110')
        }