#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script solicita ao usuário que insira um numero e imprime se ele é integer ou decimal

Funcionamento do código:

1. O usuário é solicitado a inserir um numero
2. O programa printa o valor do numero e se ele é decimal ou não
"""

number = float(input("Give me a number: "))  # Solicita um float
if number.is_integer():
    print("This number is a integer") # Imprime a frase caso ele seja um inteiro
else:
    print("This number is a decimal") # Imprime a frase caso ele seja um decimal
