from django.test import TestCase
from django.urls import reverse

from provaCarla.provaCarla.coleta.models import Coleta

class ColetaViewsTest(TestCase):
    def setUp(self):
        self.coleta = Coleta.objects.create(
            nome='Nome da Coleta',
            descricao='Descrição da Coleta',
            data='2023-01-01',
        )

    def test_listar_coletas(self):
        response = self.client.get(reverse('coletas_list'))
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta é bem-sucedida (status code 200)
        self.assertTemplateUsed(response, 'listar_coletas.html')  # Verifica se o template correto é usado
        self.assertContains(response, self.coleta.nome)  # Verifica se o nome da coleta está presente na resposta

    def test_detalhes_coleta(self):
        url = reverse('coletas_detail', args=[self.coleta.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Verifica se a resposta é bem-sucedida (status code 200)
        self.assertTemplateUsed(response, 'detalhes_coleta.html')  # Verifica se o template correto é usado
        self.assertContains(response, self.coleta.nome)  # Verifica se o nome da coleta está presente na resposta

    def test_deletar_coleta(self):
        url = reverse('coletas_delete', args=[self.coleta.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Verifica se ocorre um redirecionamento (status code 302)
        self.assertRedirects(response, reverse('coletas_list'))  # Verifica se é redirecionado para a lista de coletas
        coleta_exists = Coleta.objects.filter(pk=self.coleta.pk).exists()
        self.assertFalse(coleta_exists)  # Verifica se a coleta foi deletada (não existe mais no banco de dados)
