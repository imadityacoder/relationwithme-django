from django.db import models

# Create your models here.
class relation(models.Model):

    name=models.CharField(max_length=200)
    age = models.IntegerField()
    rel = models.CharField(max_length=200)
    date = models.DateField(default='')

    def __str__(self) -> str:
        return self.name