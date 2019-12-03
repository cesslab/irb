from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Project, Researcher


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        researchers = Researcher.objects.filter(project=self.instance)

        for i in range(len(researchers)):
            field_name = f'researcher_{i}'
            self.fields[field_name] = forms.CharField(required=False)

            try:
                self.initial[field_name] = researchers[i].project
            except IndexError:
                self.initial[field_name] = ''

        field_name = f'interest_{len(researchers) + 1}'
        self.fields[field_name] = forms.CharField(required=False)

    def save(self):
        project: Project = self.instance
        project.name = self.cleaned_data['name']
        project.previous_clearance = self.cleaned_data['previous_clearance']
        project.previous_protocol_number = self.cleaned_data['previous_protocol_number']
        project.has_deception = self.cleaned_data['has_deception']
        project.has_grant_application = self.cleaned_data['has_grant_application']
        project.grant_agency = self.cleaned_data['grant_agency']
        project.grant_release_date = self.cleaned_data['grant_release_date']


class ResearcherForm(ModelForm):
    class Meta:
        model = Researcher
        exclude = ('is_certified',)


ResearcherModelFormSet = inlineformset_factory(Project, Researcher, form=ResearcherForm, fields=['name', 'role'], extra=1, can_delete=True)
