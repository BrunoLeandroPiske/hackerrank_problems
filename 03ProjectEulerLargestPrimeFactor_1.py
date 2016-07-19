#achar maior fator primo de numero
from math import sqrt

def next_primo(atual_primo):
    new_test = True
    if (atual_primo == 2):
        new_primo = atual_primo+1
    else:
        new_primo = atual_primo+2
    while (new_test):
        if check_primo(new_primo):
            new_test = False
            return new_primo
        else:
            new_primo = new_primo +2

def check_primo(number):
    raiz = sqrt(number)
    for i in range(2,number):
        if number % i == 0:
            return False
        if i > raiz:
            return True

seq = input()

for i in range(int(seq)):
    N = input()

    cicle = True
    primo = 2
    temp = int(N)
    while (cicle):
        if temp != 1:
            if temp % primo == 0:
                temp = temp / primo
            else:
                primo = next_primo(primo)
        else:
            cicle = False

    print(primo)
