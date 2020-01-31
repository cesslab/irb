from django.db import models
from accounts.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=255)
    previous_clearance = models.BooleanField(default=False)
    previous_protocol_number = models.CharField(max_length=255, blank=True)
    has_deception = models.BooleanField(default=False)
    has_grant_application = models.BooleanField(default=False)
    grant_agency = models.CharField(max_length=255, blank=True)
    grant_release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'name: {self.name}'


class ProjectResearcher(models.Model):
    PRIMARY_INVESTIGATOR = 1
    RESEARCH_ASSISTANT = 2

    ROLE_CHOICES = (
        (PRIMARY_INVESTIGATOR, 'PI'),
        (RESEARCH_ASSISTANT, 'RA'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='researchers')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='researchers')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    is_certified = models.BooleanField(default=False)

    def role_label(self):
        return self.ROLE_CHOICES[self.role-1][1]

    def __str__(self):
        return f'User: {self.user.email}, Role: {self.role_label()}'




