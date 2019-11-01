from django.db import models
from users.models import CustomUser


class Researcher(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, null=True)
    fullname = models.CharField(max_length=255)

    def __str__(self):
        return str(self.fullname)


class ResearcherIRBProfile(models.Model):
    researcher = models.OneToOneField(Researcher, related_name='irb_profile', on_delete=models.CASCADE)
    has_irb_certification = models.BooleanField()


class Project(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProjectIRBProfile(models.Model):
    project = models.ForeignKey(Project, related_name='irb_profile', on_delete=models.CASCADE)
    previous_clearance = models.BooleanField(default=False)
    previous_protocol_number = models.CharField(max_length=255, blank=True)
    has_deception = models.BooleanField(default=False)
    has_grant_application = models.BooleanField(default=False)
    grant_agency = models.CharField(max_length=255, blank=True)
    grant_release_date = models.DateField(null=True, blank=True)


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




