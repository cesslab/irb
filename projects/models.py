from django.db import models
from users.models import CustomUser


class Researcher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Project(models.Model):
    name = models.CharField(max_length=255)
    previous_clearance = models.BooleanField()
    previous_protocol_number = models.CharField(max_length=255)
    has_deception = models.BooleanField()
    has_grant_application = models.BooleanField()
    grant_agency = models.CharField(max_length=255)
    grant_release_date = models.DateField()

    def __str__(self):
        return self.name


class ResearchGroup(models.Model):
    PRIMARY_INVESTIGATOR = 1
    RESEARCH_ASSISTANT = 2

    ROLE_CHOICES = (
        (PRIMARY_INVESTIGATOR, 'PI'),
        (RESEARCH_ASSISTANT, 'RA'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='research_group')
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE, related_name='research_group')

    def role_label(self):
        return self.ROLE_CHOICES[self.role-1][1]

    def __str__(self):
        return "{} ({})".format(self.researcher, self.ROLE_CHOICES[self.role-1][1])




