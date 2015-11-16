from django.db import models
from codesnug_2.users.models import CodesnugUser

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=50, blank=False)
    owner = models.ForeignKey(CodesnugUser, related_name='owned_tags')

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = (("title", "owner"),)
        ordering = ('title', )