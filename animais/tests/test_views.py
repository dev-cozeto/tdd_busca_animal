from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'Calpsita',
            predador = 'Não',
            venenoso = 'Não',
            domestico = 'Sim',
        )

        #Teste para que a index view está retornando as características do animal
        def test_index_view_retorna_caracteristicas_do_animal(self):
            """Teste que verifica se a index retorna as características do animal pesquisado"""
            response = self.client.get('/',
                {'buscar' : 'calopsita'}
            )
            caracteristica_animal_pesquisado = response.context['caracteristicas']
            self.assertIs(type(response.context['caracteristicas']), QuerySet)
            self.assertEqual(caracteristica_animal_pesquisado[0].nome_animal, 'calopsita')