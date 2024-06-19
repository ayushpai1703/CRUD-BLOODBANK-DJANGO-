from django import forms    
from .models import Person 
class LogForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'