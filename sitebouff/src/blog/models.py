from django.db import models


class Author(models.Model):
    pseudo = models.CharField(max_length=30)
    content = models.TextField(default=[])
    essaie_actuel = models.IntegerField(default=0)
    essaie_record = models.IntegerField(default=0)

