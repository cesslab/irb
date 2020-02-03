from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Project, ProjectResearcher
from crispy_forms.helper import FormHelper
from django import forms


class ResearcherFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ResearcherFormSetHelper, self).__init__(*args, **kwargs)
        self.use_custom_control = True
        self.form_show_labels = True
        self.form_tag = False


class ResearcherForm(ModelForm):
    class Meta:
        model = ProjectResearcher
        exclude = ('is_certified',)


class ProjectForm(ModelForm):
    instructions = forms.FileField(widget=forms.FileInput)

    class Meta:
        model = Project
        fields = ['name', 'instructions', 'description']


ProjectResearcherFormSet = inlineformset_factory(
    Project, ProjectResearcher, form=ResearcherForm, extra=1, can_delete=True)
