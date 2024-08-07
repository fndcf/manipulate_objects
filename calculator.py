#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script solicita ao usuário que insira dois numeros inteiros e imprime a soma, subtração, divisão e multiplicação dos numeros inteiros

Funcionamento do código:

1. O usuário é solicitado a inserir dois numeros inteiros
2. O programa printa o valor da soma, subtração, divisão e multiplicação dos valores solicitados
"""

first_number = int(input("Give me the first number: "))  # Solicita um inteiro
second_number = int(input("Give me the second number: "))  # Solicita um inteiro
print("Thank You!") # Imprime uma string de agradecimento
print(f"{first_number} + {second_number} =", (first_number + second_number)) # Imprime a soma dos dois inteiros solicitados
print(f"{first_number} - {second_number} =", (first_number - second_number)) # Imprime a subtração dos dois inteiros solicitados
print(f"{first_number} / {second_number} =", (first_number / second_number)) # Imprime a divisão dos dois inteiros solicitados
print(f"{first_number} * {second_number} =",(first_number * second_number)) # Imprime a multiplicação dos dois inteiros solicitados

