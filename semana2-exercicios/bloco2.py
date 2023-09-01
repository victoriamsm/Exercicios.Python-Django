#1 -- maior e menor
'''
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite mais um número: '))
if numero1 == numero2:
    print('Os números são iguais!')
elif numero1 > numero2:
    print(f'O maior entre os dois números é primeiro ==> {numero1}!')
else:
    print(f'O maior entre os dois números é o segundo ==> {numero2}!')
'''

#2 -- turno e saudações
'''
turno = input('Em que turno você estuda? [M - MATUTINO] [V - VESPERTINO] [N - NOTURNO]: ').strip().upper()[0]
if turno in 'Mm':
    print('Bom dia!')
elif turno in 'Vv':
    print('Boa tarde!')
elif turno in 'Nn':
    print('Boa noite!')
else: 
    print('Valor inválido!')
'''

#3 -- notas válidas

nota = -1
while nota < 0 or nota > 10:
    nota = float(input('Digite a nota do aluno: '))
print('Nota cadastrada com sucesso.')