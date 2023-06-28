from django.db import models
from provaCarla.provaCarla.criacao.models import Criacao

class Coleta(models.Model):
    id = models.AutoField(primary_key=True)
    criacao = models.ForeignKey(Criacao, on_delete=models.CASCADE, verbose_name="Criacao_id" )
    data = models.DateField(null=False, blank=False, verbose_name="Data")
    quantidade = models.IntegerField(blank=False,verbose_name="Quantidade")

    def str(self):
        return f"ID: {self.id}, Data: {self.data}, Quantidade: {self.quantidade}"