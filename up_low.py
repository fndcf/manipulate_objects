import math
#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script solicita ao usuário que insira uma str e transforme e printa o que for minusculo em maisculo e vice versa

Funcionamento do código:

1. O usuário é solicitado a inserir uma str
2. O programa printa o que for minusculo em maisculo e vice versa
"""

string = str(input())  # Solicita uma string
print(string.swapcase()) # Imprime uma str transformando o que for minusculo em maisculo e vice versa
