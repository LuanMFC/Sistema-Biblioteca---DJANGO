from django.contrib import admin
from Users.models import Users, Aluno, Funcionario

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_nasc', 'email', 'contato',)
    search_fields = ('name', 'email')

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'setor', 'matricula', 'cargo', )
    search_fields = ('matricula', 'user')

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('user','matricula', 'periodo', 'curso', 'devedor', 'saldo',)
    search_fields = ('name', 'email')

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Users, UserAdmin)