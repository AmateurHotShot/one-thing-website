from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'user')
        labels = {
            'title': _('')
        }

        exclude = ['user',]
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Be a success', 'class': 'form-control form-control-lg text-center font-weight-bold border-0 rounded-0'})
        }