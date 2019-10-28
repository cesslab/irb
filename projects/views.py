from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render

from .models import Project


class ProjectListView(ListView):
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    def get(self, request, *agrs, **kwargs):
        project = get_object_or_404(Project, id=kwargs['id'])
        context = {'project': project}
        return render(request, 'projects/project_detail.html', context)




