from django.contrib.postgres.fields import ArrayField
from django.db import models

def list_default():
    return ["rgb(255, 255, 255)", "rgb(0, 0, 0)"]

class Palettes(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    source = models.URLField(max_length=500)
    source_string = models.CharField(max_length=200)
    colors = ArrayField(models.CharField(max_length=50), blank=True, default=list_default)

    def __str__(self):
        return '%s' % self.name
    
    class Meta:
        ordering = ['name']
