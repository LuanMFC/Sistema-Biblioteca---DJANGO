from django.contrib import admin
from Livros.models import Livros, Genero, Emprestimo

# Register your models here.
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_pub', "photo",)
    search_fields = ('titulo',)

class GenerosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criacao',)
    search_fields = ('nome',)

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('data_emprestimo', 'data_devolucao', 'livro', 'aluno')
    search_fields = ('livro', 'aluno')

admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(Genero, GenerosAdmin)
admin.site.register(Livros, LivrosAdmin)