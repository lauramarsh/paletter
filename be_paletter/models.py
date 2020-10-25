from django.db import models

class Palettes(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    source = models.URLField()
    source_string = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name
    
    class Meta:
        ordering = ['name']

