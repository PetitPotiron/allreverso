import os
import sys
import unittest
sys.path.insert(0, os.path.dirname('/'.join(__file__.split('/')[:-1])))
import allreverso

client = allreverso.ReversoClient()

class TestCaseModule(unittest.TestCase):
    def test_translate(self):
        '''
            Test du fonctionnalité de traduction
        '''
        res = client.translate("fr", "en", "Bonjour !")
        ''' ce fonction retourne un liste, pour anticiper une changement
        on verifie que c'est bien un donnée de type `list` '''
        self.assertTrue(isinstance(res, list))
        # On verifie qu'il y a bien une reponse dans la liste.
        self.assertTrue(res[0])
    
    def test_correct(self):
        '''
            Test du fonctionnalité de correction de texte
        '''
        res = client.correct("fr", "Bonjoure !").text
        # verification que le resultat existe
        self.assertTrue(res)
    
    def test_define(self):
        '''
            Test du fonctionnalité du defintion
        '''
        res = client.define("en", "boat")
        # verification que le resultat existe
        self.assertTrue(res)
    
    def test_synonymize(self):
        '''
            Test du fonctionnalité de synonyme
        '''
        res = client.synonymize("fr", "bateau")
        # verification que le resultat existe
        self.assertTrue(res)


if __name__ == '__main__':
    runner = unittest.TestCase()
    runner.run()

