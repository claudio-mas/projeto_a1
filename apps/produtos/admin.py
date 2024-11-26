from django.contrib import admin
from .models import Marca, Produto, Opcional, Periferico


# Register your models here.
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'logo', 'revenda')
    list_editable = ('logo', 'revenda')
    search_fields = ('marca', 'revenda')
    list_per_page = 10


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('ref', 'produto', 'descricao', 'precounit')
    list_editable = ('produto', 'descricao', 'precounit')
    search_fields = ('ref', 'produto', 'descricao')
    list_per_page = 10


class OpcionalAdmin(admin.ModelAdmin):
    list_display = ('ref', 'opcional', 'precounit')
    list_editable = ('opcional', 'precounit')
    search_fields = ('ref', 'opcional')
    list_per_page = 10


class PerifericoAdmin(admin.ModelAdmin):
    list_display = ('ref', 'periferico', 'precounit')
    list_editable = ('periferico', 'precounit')
    search_fields = ('ref', 'periferico')
    list_per_page = 10


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Opcional, OpcionalAdmin)
admin.site.register(Periferico, PerifericoAdmin)
