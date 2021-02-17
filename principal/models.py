from django.db import models

class Config(models.Model):
    variavel = models.CharField(max_length=50)
    valor = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.variavel
