from django.contrib import admin
from .models import Orcamento, ItensOrcamento


class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'data', 'valor')
    list_editable = ('data', 'valor')
    fieldsets = (
        ('Dados do Orçamento', {
            'fields': ('numero', 'data', 'valor', 'validade', 'status', 'observacao')
        }),
        ('Dados do Pedido', {
            'fields': ('pedido', 'datapedido')
        }),
        ('Dados do Contrato', {
            'fields': ('contrato', 'datacontrato', 'pdf_contrato')
        }),
    )


admin.site.register(Orcamento, OrcamentoAdmin)
admin.site.register(ItensOrcamento)
