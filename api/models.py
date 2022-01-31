from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    sobrenome = models.CharField(max_length=50, blank=False)
    datanascimento = models.DateField(blank=False)
    naturalidade = models.CharField(max_length=50, blank=False)
    hobby = models.CharField(max_length=50, blank=True)
    
    def __str__(self) -> str:
        return self.nome
