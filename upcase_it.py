#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script solicita ao usuário que insira uma palavra e retorna essa palavra em letra maiuscula.

Funcionamento do código:

1. O usuário é solicitado a inserir uma string
2. O programa transforma a string para letra maiuscula
"""

word= str(input("Give me a word: "))  # Solicita uma string
print(f"{word.upper()}") # Imprime a string com letra maiscula
