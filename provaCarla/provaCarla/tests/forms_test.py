from django.test import TestCase
from datetime import date

from provaCarla.provaCarla.coleta.models import Coleta


class ColetaFormsTest(TestCase):
    def test_form_criacao_coleta(self):
        form_data = {
            'nome': 'Nome da Coleta',
            'descricao': 'Descrição da Coleta',
            'data': date.today(),
        }
        form = ColetaForm(data=form_data)
        self.assertTrue(form.is_valid())  # Verifica se o formulário é válido

        # Cria uma coleta com os dados do formulário
        coleta = form.save()

        # Verifica se a coleta foi salva corretamente
        self.assertEqual(coleta.nome, form_data['nome'])
        self.assertEqual(coleta.descricao, form_data['descricao'])
        self.assertEqual(coleta.data, form_data['data'])

    def test_form_edicao_coleta(self):
        coleta = Coleta.objects.create(
            nome='Nome da Coleta',
            descricao='Descrição da Coleta',
            data=date.today(),
        )

        form_data = {
            'nome': 'Novo Nome da Coleta',
            'descricao': 'Nova Descrição da Coleta',
            'data': date.today(),
        }
        form = ColetaForm(data=form_data, instance=coleta)
        self.assertTrue(form.is_valid())  # Verifica se o formulário é válido

        # Salva as alterações no objeto coleta
        form.save()

        # Recarrega o objeto coleta do banco de dados
        coleta.refresh_from_db()

        # Verifica se as alterações foram salvas corretamente
        self.assertEqual(coleta.nome, form_data['nome'])
        self.assertEqual(coleta.descricao, form_data['descricao'])
        self.assertEqual(coleta.data, form_data['data'])

    def test_form_criacao_coleta_data_futura(self):
        form_data = {
            'nome': 'Nome da Coleta',
            'descricao': 'Descrição da Coleta',
            'data': date.today() + timedelta(days=1),  # Data futura
        }
        form = ColetaForm(data=form_data)
        self.assertFalse(form.is_valid())  # Verifica se o formulário é inválido

    def test_form_criacao_coleta_duplicada(self):
        coleta = Coleta.objects.create(
            nome='Nome da Coleta',
            descricao='Descrição da Coleta',
            data=date.today(),
        )

        form_data = {
            'nome': 'Nome da Coleta',
            'descricao': 'Nova Descrição da Coleta',
            'data': date.today(),
        }
        form = ColetaForm(data=form_data)
        self.assertFalse(form.is_valid())  # Verifica se o formulário é inválido
