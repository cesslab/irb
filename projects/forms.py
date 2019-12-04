from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Project, Researcher


class ResearcherForm(ModelForm):
    class Meta:
        model = Researcher
        exclude = ('is_certified',)


ResearcherModelFormSet = inlineformset_factory(
    Project, Researcher, form=ResearcherForm, extra=1, can_delete=True)
