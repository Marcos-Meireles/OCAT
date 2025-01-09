from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Produto")
    quantidade_em_estoque = models.IntegerField(default=0, verbose_name="Quantidade em Estoque")
    disponivel = models.BooleanField(default=True, verbose_name="Está disponível?")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    
    CATEGORIAS = [
        ('EL', 'Eletrônicos'),
        ('CL','Casa e Lazer'),
        ('MT','Material Escolar'),
        ('OU','Outros')
    ]
    
    categoria = models.CharField(max_length=2, choices=CATEGORIAS, default='OU', verbose_name="Categoria")
    
    
    def __str__(self):
        return self.nome
