from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Leitor (models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    dataNascimento = models.DateField()
    descricao = models.CharField(max_length=255)

class Livro (models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    data_Pub = models.DateField()

class Emprestimo (models.Model):
    devolvido = models.BooleanField()
    dataEmprestimo = models.DateTimeField()
    dataDevolucao = models.DateTimeField()
    ledor = models.ForeignKey(Leitor, on_delete=models.CASCADE)