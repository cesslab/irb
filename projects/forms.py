from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Project, ProjectResearcher


class ResearcherForm(ModelForm):
    class Meta:
        model = ProjectResearcher
        exclude = ('is_certified',)


ResearcherModelFormSet = inlineformset_factory(
    Project, ProjectResearcher, form=ResearcherForm, extra=1, can_delete=True)
