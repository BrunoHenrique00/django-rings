from django.contrib import admin
from .models import Anel

@admin.register(Anel)
class AnelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'poder', 'portador', 'forjadoPor', 'imagem')
    search_fields = ('nome', 'portador', 'forjadoPor')
    list_filter = ('forjadoPor',)
