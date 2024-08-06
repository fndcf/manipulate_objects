import math
#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script solicita ao usuário que insira um float e caso tenha casas decimais apresenta o valor arredondado para cima

Funcionamento do código:

1. O usuário é solicitado a inserir um float
2. O programa printa o valor arrendondado para cima do float
"""

number = float(input("Give me a number: "))  # Solicita um float
print(int(math.ceil((number)))) # Imprime um int sempre arredondado para cima
