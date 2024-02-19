from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null= False)
    year = models.IntegerField(max_length=2, null=False)
    date_nasc = models.DateField(null=False)
    email = models.EmailField(null=False)
    contato = models.CharField(null=False)

    def __str__(self):
        return self.name
    

class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null= False)
    matricula = models.CharField(max_length=20, null= False)
    cargo = models.CharField(max_length=50, null=False)
    date_contrato = models.DateField(null=False)

    def __str__(self):
        return self.name
    

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null= False)
    matricula = models.CharField(max_length=200, null= False)
    periodo = models.CharField(max_length=6, null=False)
    devedor = models.BooleanField(null=False)
    saldo = models.DecimalField(null=False)

    def __str__(self):
        return self.name