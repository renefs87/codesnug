from django.db import models
from django.core.urlresolvers import reverse

from codesnug_2.auth.models import CodesnugUser
from codesnug_2.goals.constants import WORKSPACE_PERMISSIONS, LANGUAGE_CHOICES


class Tag(models.Model):
    title = models.CharField(max_length=50, blank=False)
    owner = models.ForeignKey(CodesnugUser, related_name='owned_tags')

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = (("title", "owner"),)
        ordering = ('title', )


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


class Goal(models.Model):
    owner = models.ForeignKey(CodesnugUser, related_name='owned_goals')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='goals')
    workspaces = models.ManyToManyField(Workspace, blank=True, related_name='goals')
    is_private = models.BooleanField(default=True)

    class Meta:
        unique_together = (("title", "owner"),)
        ordering = ('created_at', )

    def __unicode__(self):
        return self.id

    def get_absolute_url(self):
        url = reverse("goal_detail", args=[str(self.id), str(self.owner.username)])
        return url


class BaseSnippet(models.Model):
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='text')
    version_number = models.IntegerField(default=1)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id

    class Meta:
        abstract = True
        ordering = ('created_at', )


class Snippet(BaseSnippet):
    author = models.ForeignKey(CodesnugUser, related_name='owned_snippets')
    goal = models.ForeignKey(Goal, related_name='snippets')
    title = models.CharField(max_length=200)


class Version(BaseSnippet):
    author = models.ForeignKey(CodesnugUser, related_name='owned_versions')
    snippet = models.ForeignKey(Snippet, related_name='versions')

    class Meta:
        unique_together = (("snippet", "version_number"),)