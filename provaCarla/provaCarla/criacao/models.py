from django.db import models

class Criacao(models.Model):
    id = models.AutoField(primary_key=True)
    raca = models.CharField(max_length=100, null=False, blank=False, verbose_name="Raca")
    data_entrada = models.DateField(null=False, blank=False, verbose_name="Data_entrada")

    def str(self):
        return f"ID: {self.id}, Raça: {self.raca}, Data de Entrada: {self.data_entrada}"