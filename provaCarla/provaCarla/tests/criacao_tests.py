from django.test import TestCase

from provaCarla.provaCarla.coleta.models import Coleta


class ColetaCriacaoTest(TestCase):
    def test_tamanho_maximo_caracteres(self):
        coleta = Coleta.objects.create(
            nome='Nome da coleta com um texto muito longo para exceder o limite máximo de caracteres',
            descricao='Descrição da coleta',
            data='2023-01-01',
        )
        max_length = coleta._meta.get_field('nome').max_length
        self.assertEqual(len(coleta.nome), max_length)  # Verifica se o tamanho do nome é igual ao limite máximo

    def test_elementos_obrigatorios(self):
        with self.assertRaises(ValueError):
            Coleta.objects.create()  # Tenta criar uma coleta sem fornecer valores obrigatórios

    def test_verbose_name(self):
        nome_field = Coleta._meta.get_field('nome')
        self.assertEqual(nome_field.verbose_name, 'nome')  # Verifica se o verbose_name é 'nome'

    def test_ordem_coletas(self):
        coleta1 = Coleta.objects.create(
            nome='Nome da coleta 1',
            descricao='Descrição da coleta 1',
            data='2023-01-01',
        )
        coleta2 = Coleta.objects.create(
            nome='Nome da coleta 2',
            descricao='Descrição da coleta 2',
            data='2023-01-02',
        )
        coleta3 = Coleta.objects.create(
            nome='Nome da coleta 3',
            descricao='Descrição da coleta 3',
            data='2023-01-03',
        )

        coletas_ordenadas = Coleta.objects.all().order_by('-data')
        self.assertEqual(coletas_ordenadas[0], coleta3)  # Verifica se a coleta mais recente é a coleta3
        self.assertEqual(coletas_ordenadas[1], coleta2)  # Verifica se a segunda coleta mais recente é a coleta2
        self.assertEqual(coletas_ordenadas[2], coleta1)  # Verifica se a terceira coleta mais recente é a coleta1
