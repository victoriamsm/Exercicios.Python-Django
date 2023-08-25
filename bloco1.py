#1 -- input /fstring
'''
numero = int(input('Digite um número: '))
print(f'O número digitado foi {numero}')
'''

#2 -- soma simples
'''
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
s = valor1 + valor2
print(f'A expressao é: {valor1} + {valor2} = {s}')
'''

#3 -- celsius
'''
c = int(input('Digite a temperatura em Celsius: '))
f = (c * 1.8) + 32
print(f'{c}º Celsius vale {f}º Fahrenheit.')
'''

#4 -- salário

valor = float(input('Quanto você ganha por hora? R$'))
horas = int(input('Quantas horas você trabalha por dia? '))
mes = horas*30
sal = mes * valor
print(f'Seu salário por mês é de R${sal:.2f}.')
