#1 -- soma função
'''
def soma(a,b,c):
    s = a + b + c
    print(f'O resultado da soma é {s}')

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

soma(a,b,c)
'''

#2 -- inverso função
'''
def inverso(num):
    num1 = str(num)
    num1 = num1[::-1]    
    print(f'O inverso de {num} é {num1}!')

num = int(input('Digite um número para descobrir seu inverso: '))
inverso(num)
'''

#3 -- celsius função

def menu():
    print(' ** MENU DE CONVERSÕES **')
    print(' [1] Converter para FAHRENHEIT ')
    print(' [2] Converter para CELSIUS')
    resp = int(input('Digite a opção desejada: '))
    if resp == 1:
        fahrent()
    elif resp == 2:
        celsius()

def fahrent():
    temp = float(input('Temperatura em CELSIUS: '))
    f = (temp * 1.8) + 32
    print(f'==> {temp}º Celsius é equivalente a {f:.1f}º Fahrenheit.')

def celsius():
    temp = float(input('Temperatura em FAHRENHEIT: '))
    c = (temp - 32) / 1.8
    print(print(f'==> {temp}º Fahrenheit é equivalente a {c:.1f}º Celsius.'))

menu()    
