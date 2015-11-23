from django.db import models

from codesnug_2.auth.models import CodesnugUser


class Workspace(models.Model):
    owner = models.ForeignKey(CodesnugUser, related_name='owned_workspaces')
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = (("title", "owner"),)
        ordering = ('title', )