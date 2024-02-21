from django.db import models


class IES(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null= False)
    data_criacao = models.CharField(max_length=200, null=False)
    cnpj = models.CharField(max_length=200, null=False)
    estado = models.CharField(max_length=200, null=False)
    cidade = models.CharField(max_length=200, null=False)
    endereco = models.CharField(max_length=200, null=False)
    telefone = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.nome
    
class Setor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null= False)
    data_criacao = models.CharField(max_length=200, null=False)
    ies = models.ForeignKey(IES, on_delete = models.PROTECT, related_name="setor_ies")

    def __str__(self):
        return self.nome