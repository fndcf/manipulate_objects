#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
Este script solicita ao usuário que insira sua idade como um numero inteiro e printa a idade em 10,20 e 30 anos

Funcionamento do código:

1. O usuário é solicitado a inserir um numero inteiro
2. O programa printa sua idade atual e sua idade em 10,20 e 30 anos
"""

"""
age= int(input("Please tell me your age: "))  # Solicita um inteiro
print("You are currently",age, "years old.") # Imprime uma string contendo sua idade atualmente
print("In 10 years, you'll be",age + 10, "years old.") # Imprime uma string contendo sua idade em 10 anos
print("In 20 years, you'll be",age + 20, "years old.") # Imprime uma string contendo sua idade em 20 anos
print("In 30 years, you'll be",age + 30, "years old.") # Imprime uma string contendo sua idade em 30 anos
"""

age= int(input("Please tell me your age: "))  # Solicita um inteiro
print(f"You are currently {str(age)} years old.") # Imprime uma string contendo sua idade atualmente
for count in range(10, 40, 10):  # Itera de 10 a 30 em intervalos de 10 em 10
    print("In", str(count), "years, you'll be",str((age + (count))), "years old")  # Imprime uma string contendo sua idade em 10,20 e 30 anos
