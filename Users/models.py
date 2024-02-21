from django.db import models

from IES.models import Setor

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null= False)
    date_nasc = models.DateField(null=False)
    email = models.EmailField(null=False)
    contato = models.CharField(max_length=20,null=False)
    estado = models.CharField(max_length=50,null=False,default='')
    cidade = models.CharField(max_length=50,null=False, default='')
    endereco = models.CharField(max_length=200,null=False,default='')

    def __str__(self):
        return self.name + ' ' + self.email
    

class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=20, null= False)
    cargo = models.CharField(max_length=50, null=False)
    date_contrato = models.DateField(null=False)
    user = models.ForeignKey(Users, on_delete = models.PROTECT, related_name = "users_funcionarios")
    setor = models.ForeignKey(Setor, on_delete = models.PROTECT, related_name = 'setor_funcionario', default="0")
    def __str__(self):
        return self.matricula
    

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=200, null= False)
    periodo = models.CharField(max_length=6, null=False)
    curso = models.CharField(max_length=200, null= False)
    devedor = models.BooleanField(null=False)
    saldo = models.FloatField(null=False)
    user = models.ForeignKey(Users, on_delete=models.PROTECT, related_name="users_aluno")
    def __str__(self):
        return self.matricula