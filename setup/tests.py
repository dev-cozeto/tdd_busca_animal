from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):
   
   #Função que inicia o driver
    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe')
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'

        )

   #Função que fecha o browser
    def tearDown(self):
        self.browser.quit()

    # #Função teste para abrir janela
    # def test_abre_janela_chrome():
    #     self.browser.get(self.live_server_url)

    # #Função de teste que falha
    # def test_deu_ruim(self):
    #     """teste de exemplo de erro"""
    #     self.fail('Teste Falhou - deu ruim mesmo !!!')

    #Teste para  buscar um novo animal
    def test_bucando_um_novo_Animal(self):
        """ TESTE SE UM USUÁRIO ENCONTRA UM ANIMAL NA PESQUISA"""



        #Vini, deseja encontrar um novo animal, para adotar. 

        #Ele encontra o Busca Animal e decide usar o site, 
        home_page = self.browser.get(self.live_server_url + '/')
        #Porque ele ve no menu do site escrito Buca Animal
        brand_element = self.browser.find_element(By.CSS_SELECTOR, 'navbar')
        self.assertEqual('Busca Animal', brand_element.text())

        #Ele ve um campo para pesquisar animais pelo nome. 
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão')

        #Ele pesquisa por Leão e clica no botao pesquisar.
        buscar_animal_input.send_keys('leão')
        # time.sleep()
        self.browser.find_element(By.CSS_SELECTOR,'form button').click()

        #O site exibe 4 características do animal pesquisado. 
        características = self.browser.find_elements(By.CSS_SELECTOR, '.results_description')
        self.assertGreater(len(características), 3)

        #Ele desiste de adotar um leão. 