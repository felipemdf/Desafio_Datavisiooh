from django.contrib import admin
from api.models import Pessoa

class Pessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'datanascimento', 'naturalidade','hobby')
    list_display_links = ('id', 'nome', 'sobrenome', 'datanascimento', 'naturalidade','hobby')
    search_fields = ('id', 'nome', 'sobrenome', 'datanascimento', 'naturalidade','hobby')
    list_per_page = (5)

admin.site.register(Pessoa, Pessoas)
