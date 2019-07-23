from unittest import TestCase
# from unittest.mock import Mock, patch

from func import formatar_dados, pegar_menor_item
from errors import DataNotProvided, IsNotADictionary, MinItemValueNotFound

class TestProcessar(TestCase):

    sample_dict_one = {'VIAGEM': -430.49, 'DIVERSAO': -262.23, 'ALIMENTACAO': -329.02, 'HOSPEDAGEM': -1573.44, 'VESTUARIO': -59.95, 'TRANSPORTE': -83.14, 'HIGIENE': -28.07}
    sample_dict_two = {'Feb': -430.49, 'Mar': -571.84, 'Apr': -59.95, 'May': -1704.5100000000002, 'Jun': -22.810000000000002}
    
    def get_data_from_file(self):

        with open('./movimentacao.log') as log_file:

            return log_file.readlines()

    def test_formatar_dados_sem_dados(self):

        with self.assertRaises(DataNotProvided):
            
            dados_formatados = formatar_dados('')

    def test_formatar_dados(self):
    
        dados_formatados = formatar_dados(self.get_data_from_file())

        total_lines = len(dados_formatados.split('\n'))

        self.assertIsInstance(dados_formatados, str)
        self.assertEqual(total_lines, 31)
    
    def test_pegar_menor_item_sem_dicionario(self):

        with self.assertRaises(IsNotADictionary):
            pegar_menor_item('')
        with self.assertRaises(IsNotADictionary):
            pegar_menor_item(12)
        with self.assertRaises(IsNotADictionary):
            pegar_menor_item([])

    def test_pegar_menor_item(self):

        self.assertEqual(pegar_menor_item(self.sample_dict_one), 'HOSPEDAGEM')
        self.assertEqual(pegar_menor_item(self.sample_dict_two), 'May')
        

