from unittest import TestCase

n1 = 1
n2 = 1

class Main():
    def soma(n1,n2):
        resultado = n1+n2
        print(f'{n1} + {n2} = {resultado}')
        return resultado
    
    def subtracao(n1,n2):
        resultado = n1-n2
        print(f'{n1} - {n2} = {resultado}')
        return resultado
    
    def multiplicacao(n1,n2):
        resultado = n1*n2
        print(f'{n1} * {n2} = {resultado}')
        return resultado
    
    def divisao(n1,n2):
        resultado = n1/n2
        print(f'{n1} / {n2} = {resultado}')
        return resultado

class TestMain(TestCase):
  def testSoma(self):
    # 1 + 1 => 2
    self.assertEqual(Main.soma(1,  1), 2)
  
  def testSubtracao(self):
    # 1 - 1 => 0
    self.assertEqual(Main.subtracao(1, 1), 0)

  def testMultiplicacao(self):
    # 1 * 1 => 1
    self.assertEqual(Main.multiplicacao(1, 1), 1)
 
  def testDivisao(self):
    # 1 / 1 => 1
    self.assertEqual(Main.divisao(1, 1), 1) 

Main();
TestMain();
