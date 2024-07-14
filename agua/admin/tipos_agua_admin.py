from django.contrib import admin

from ..models import TiposAgua


# @admin.register(TiposAgua)
class TiposAguaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
    ]

    search_fields = [
        'id',
        'titulo'
    ]
