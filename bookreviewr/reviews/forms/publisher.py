from django import forms
from ..models import DBPublisher

class PublisherForm(forms.ModelForm):
    
    class Meta:
        model = DBPublisher
        fields = "__all__"
