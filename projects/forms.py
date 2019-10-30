from django import forms
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    previous_clearance = forms.BooleanField(required=False)
    previous_protocol_number = forms.CharField(max_length=255, required=False)
    has_grant_application = forms.BooleanField(required=False)
    grant_agency = forms.BooleanField(required=False)
    grant_release_date = forms.DateField(required=False)

    class Meta:
        model = Project
        fields = [
            'name', 'previous_clearance', 'previous_protocol_number', 'has_deception', 'has_grant_application',
            'grant_agency', 'grant_release_date'
        ]
