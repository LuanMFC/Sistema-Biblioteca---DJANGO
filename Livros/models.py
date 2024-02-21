from django.db import models
from Users.models import Aluno

# Create your models here.


class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null= False)
    data_criacao = models.DateField(null=False)

    def __str__(self):
        return self.nome

class Livros(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, null= False)
    autor = models.CharField(max_length=200, null= False)
    editora = models.CharField(max_length=200, null= False)
    data_pub = models.DateField(null= False)
    photo = models.ImageField(upload_to="media/")
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name = "genero_livro")
    def __str__(self):
        return self.titulo
    
class Emprestimo(models.Model):
    id = models.AutoField(primary_key=True)
    data_emprestimo = models.DateField(null=False)
    prazo = models.CharField(max_length=200, null= False)
    taxaMulta  = models.CharField(max_length=200, null= False)
    data_devolucao = models.DateField(null=False)
    multa = models.CharField(max_length=200, null= False)
    livro = models.ForeignKey(Livros, on_delete=models.PROTECT, related_name = "livro_emprestimo")
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, related_name = "aluno_emprestimo")
