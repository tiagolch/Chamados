from django.contrib import admin
from .models import *


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    pass


@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    pass


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Abertura)
class AberturaAdmin(admin.ModelAdmin):
    pass


