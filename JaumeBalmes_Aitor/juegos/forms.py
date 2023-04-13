from django.forms import ModelForm
from .models import Students

class PersonForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'