from django.db import models

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Rule(Base):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    point = models.FloatField()

    def __str__(self):
        return f'{self.name} - {self.description} - {self.point}'
