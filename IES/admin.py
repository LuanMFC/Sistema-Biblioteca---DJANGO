from django.contrib import admin

from IES.models import IES, Setor

# Register your models here.
class IESAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'data_criacao', 'telefone', 'email',)
    search_fields = ('nome', 'cnpj',)

class SetorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ies',)
    search_fields = ('nome',)



admin.site.register(Setor, SetorAdmin)
admin.site.register(IES, IESAdmin)