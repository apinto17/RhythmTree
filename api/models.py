from django.db import models
import uuid
from django.conf import settings


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False, blank=False)
    master_version = models.ForeignKey("Version", null=True, on_delete=models.SET_NULL, related_name="master_project")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    date_modified = models.DateField(null=False, blank=False, auto_now=True)

    def save(self, *args, **kwargs):
        if(self.master_version is None):
            self.master_version = Version.objects.create(name="Default", project=self.id)
        super().save(*args, **kwargs)


class Version(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(
        "Project",
        null=False,
        on_delete=models.CASCADE,
        related_name="versions"
    )
    name = models.TextField(null=False, blank=False)
    date_created = models.DateField(null=False, blank=False, auto_now_add=True)


class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False, blank=False)
    length = models.TextField(null=False, blank=False)
    # TODO create custom on_delete function
    version = models.ForeignKey(
        "Version",
        null=False,
        on_delete=models.CASCADE,
        related_name="tracks"
    )
