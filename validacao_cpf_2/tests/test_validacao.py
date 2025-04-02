import unittest
from app.validacao import validar_cpf 

class TestValidarCPF(unittest.TestCase):
    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("52998224725"))
        self.assertTrue(validar_cpf("12345678909"))
    
    def test_cpf_invalido(self):
        self.assertFalse(validar_cpf("11111111111"))
        self.assertFalse(validar_cpf("52998224724"))
        self.assertFalse(validar_cpf("123456"))
        self.assertFalse(validar_cpf("abcd.efg.hij-kl"))
    
    def test_cpf_vazio(self):
        self.assertFalse(validar_cpf(""))
    
if __name__ == "__main__":
    unittest.main()
