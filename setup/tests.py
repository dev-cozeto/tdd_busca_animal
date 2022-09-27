from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
   
   #Função que inicia o driver
    def setUp(self):
        self.browser = webdriver.ChromiumEdge('msedgedriver.exe')

   #Função que fecha o browser
    def tearDown(self):
        self.browser.quit()

    #Função teste para abrir janela
    def test_abre_janela_chrome():
        self.browser.get(self.live_server_url)

    #Função de teste que falha
    def test_deu_ruim(self):
        """teste de exemplo de erro"""
        self.fail('Teste Falhou - deu ruim mesmo !!!')