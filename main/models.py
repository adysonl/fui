from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    uf = models.CharField(max_length=15)

    def __str__(self):
        return self.cidade + " " + self.uf

class Usuario(models.Model):
    TIPO_CHOICES=(
        ("kg" , "King"),
        ("am" , "Animal")
    )

    user = models.OneToOneField(User, related_name="user", on_delete=models.PROTECT)
    tipo = models.CharField(max_length=6, choices=TIPO_CHOICES)
    endereco = models.OneToOneField(Endereco, related_name="endereco", on_delete=models.PROTECT, blank=True, null=True)
    rg = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.fist_name + " " + self.user.last_name