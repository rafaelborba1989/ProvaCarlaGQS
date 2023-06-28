from django.test import TestCase

from provaCarla.provaCarla.coleta.models import Coleta


class ColetaModelTest(TestCase):
    def setUp(self):
        # Crie um objeto coleta para usar nos testes
        self.coleta = Coleta.objects.create(
            nome='Nome da coleta',
            descricao='Descrição da coleta',
            data='2023-01-01',
        )

    def test_tamanho_maximo_caracteres(self):
        max_length = self.coleta._meta.get_field('nome').max_length
        self.assertEqual(max_length, 100)  # Verifica se o tamanho máximo é 100 caracteres

    def test_elementos_obrigatorios(self):
        coleta = Coleta.objects.create()  # Cria uma coleta vazia
        self.assertRaises(ValueError, coleta.full_clean)  # Verifica se ocorre uma exceção ValueError

    def test_verbose_name(self):
        nome_field = self.coleta._meta.get_field('nome')
        self.assertEqual(nome_field.verbose_name, 'nome')  # Verifica se o verbose_name é 'nome'

    def test_ordem_coletas(self):
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
        self.assertEqual(coletas_ordenadas[2], self.coleta)  # Verifica se a terceira coleta mais recente é a coleta criada no setUp
