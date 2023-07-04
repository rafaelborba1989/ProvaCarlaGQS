from django import forms
from datetime import date, timedelta
from .models import Coleta, Criacao


class ColetaForm(forms.ModelForm):
    class Meta:
        model = Coleta
        fields = ['nome', 'descricao', 'data']

    def clean_data(self):
        data = self.cleaned_data['data']
        if data > date.today():
            raise forms.ValidationError("A data não pode ser futura.")
        return data

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if Coleta.objects.filter(nome=nome).exists():
            raise forms.ValidationError("Já existe uma coleta com este nome.")
        return nome


class CriacaoForm(forms.ModelForm):
    class Meta:
        model = Criacao
        fields = ['raca', 'data_entrada']

    def clean_data_entrada(self):
        data_entrada = self.cleaned_data['data_entrada']
        if data_entrada > date.today():
            raise forms.ValidationError("A data de entrada não pode ser futura.")
        return data_entrada
