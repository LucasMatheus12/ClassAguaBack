from django.contrib import admin

from ..models import TabelaAgua


@admin.register(TabelaAgua)
class TabelaAguaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome'
    ]
