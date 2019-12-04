from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, render

from django.db import transaction

from .models import Project
from .forms import ResearcherModelFormSet


class ProjectListView(ListView):
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    def get(self, request, *agrs, **kwargs):
        project = get_object_or_404(Project, id=kwargs['id'])
        context = {'project': project}
        return render(request, 'projects/project_detail.html', context)


class ProjectResearcherCreateView(CreateView):
    model = Project
    fields = ['name']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')

    def get_context_data(self, **kwargs):
        data = super(ProjectResearcherCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['researchers'] = ResearcherModelFormSet(self.request.POST)
        else:
            data['researchers'] = ResearcherModelFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        researchers = context['researchers']
        with transaction.atomic():
            self.object = form.save()

            if researchers.is_valid():
                researchers.instance = self.object
                researchers.save()
            return super(ProjectCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'id': self.object.id})
