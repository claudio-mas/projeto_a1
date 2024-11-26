from django.db import models


class Orcamento(models.Model):
    TIPO_STATUS = (
        ('Em Andamento', 'Em Andamento'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
        ('Cancelado', 'Cancelado'),
    )
    id = models.AutoField(primary_key=True)
    # IDCliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='orcamento_cliente_fk', default=1)
    # IDVendedor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='vendedor_fk')
    # idmarca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='orcamento_marca_fk', default=1)
    numero = models.CharField(max_length=10, verbose_name='Nº Orçamento')
    data = models.DateField(blank=True, null=True, verbose_name='Data')
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0, verbose_name='Valor')
    validade = models.DateField(blank=True, null=True, verbose_name='Validade')
    status = models.CharField(max_length=20, blank=True, null=True, default='Em Andamento', choices=TIPO_STATUS, verbose_name='Status')
    pedido = models.CharField(max_length=10, blank=True, null=True, default='-', verbose_name='Nº Pedido')
    datapedido = models.DateField(blank=True, null=True, verbose_name='Data do Pedido')
    contrato = models.CharField(max_length=10, blank=True, null=True, default='-', verbose_name='Nº Contrato')
    datacontrato = models.DateField(blank=True, null=True, verbose_name='Data do Contrato')
    pdf_contrato = models.FileField(upload_to='orcamentos/', blank=True, null=True, verbose_name='PDF Contrato')
    observacao = models.TextField(blank=True, null=True, verbose_name='Observações')

    class Meta:
        verbose_name_plural = "3.1- Orçamentos"
        verbose_name = "Orçamento"

    def __str__(self):
        return f'Orcamento {self.ID} - {self.IDCliente} - {self.Data} - {self.Valor}'


class ItensOrcamento(models.Model):
    id = models.AutoField(primary_key=True)
    # IDOrcamento = models.ForeignKey(Orcamento, on_delete=models.PROTECT, related_name='orcamento_fk')
    # IDProduto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='itens_produto_fk')
    quantidade = models.IntegerField()
    valorunitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valortotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "3.2- Itens do Orçamento"
        verbose_name = "Item do Orçamento"

    def __str__(self):
        return f'Item {self.ID} - {self.IDOrcamento} - {self.IDProduto} - {self.Quantidade}'
