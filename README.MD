# Calculadora basica

Para iniciar, foi realizado um pequeno estudo sobre testes em linguagem python, nos deparamos com apenas 2 bibliotecas para teste unitário, o UnitTest e o PyUnit, logo após isso demos inicio ao projeto, uma simples calculadora onde o usuário coloca os dois valores e é mostrado na tela as quatro operações.

A seguir leia os comandos para dar inicio aos testes

## Como usar

### Teste Padrão

``` python
pytest -vv test_main.py
```

----------

### Teste com cobertura de linha(nós)

```python
pythonpytest -vv test_main.py --cov=calculadora
```

----------

### Teste com cobertura de ramos(branchs)

```python

pytest -vv test_main.py --cov=calculadora --cov-branch --cov-report html

```

----------

### Teste com MutMut

#### Não consegui fazer rodar o teste de mutação com mutmut, nem com o mutpy

```python
mutmut run --paths-to-mutate= [path]

mut.py --target calculadora --unit-test test_main -m
```

>> Made By Eder Ramos Filho, Eduardo Paterno e Rosangela Furtado.
