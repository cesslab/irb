from django.urls import path


from .views import ProjectListView, ProjectDetailView, ProjectResearcherCreateView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<int:id>', ProjectDetailView.as_view(), name='project_detail'),
    path('create', ProjectResearcherCreateView.as_view(), name='project_create'),
]
