from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from django.db import transaction

from .models import Project
from .forms import ProjectResearcherFormSet, ResearcherFormSetHelper, ProjectForm


class ProjectListView(LoginRequiredMixin, ListView):
    queryset = Project.objects.all()


class ProjectDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, *agrs, **kwargs):
        project = get_object_or_404(Project, id=kwargs['id'])
        context = {'project': project}
        return render(request, 'projects/project_detail.html', context)


class ProjectResearcherCreateView(LoginRequiredMixin, CreateView):
    model = Project
    # fields = ['name', 'description', 'instructions']
    template_name = 'projects/project_researchers_create.html'
    success_url = reverse_lazy('project_list')
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        data = super(ProjectResearcherCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['project_researcher_formset'] = ProjectResearcherFormSet(self.request.POST)
        else:
            data['project_researcher_formset'] = ProjectResearcherFormSet()

        data['helper'] = ResearcherFormSetHelper()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['project_researcher_formset']
        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.save()

            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            return super(ProjectResearcherCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('projects:project_detail', kwargs={'id': self.object.id})
