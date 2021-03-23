from django.db import models

# Create your models here.

class Questions(models.Model):
    enunciated = models.TextField()
    available = models.BooleanField(default=False)
    alternatives = models.JSONField()
    correct_alternative = models.IntegerField(choices=[
        {0, "A"},
        {1, "B"},
        {3, "C"},
        {4, "D"},
    ])

    def __str__(self):
        return self.enunciated