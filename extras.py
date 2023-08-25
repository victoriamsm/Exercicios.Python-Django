#1 -- conversões de moedas
'''
def conversor():
    print(' ** CONVERSOR DE MOEDAS ** ')
    qntReal = float(input('Quantos reais você tem na carteira? R$'))
    dEua = qntReal/4.91
    pArg = qntReal/0.02
    dAus = qntReal/3.18
    dCan = qntReal/3.64
    fSui = qntReal/0.42 #??
    euro = qntReal/5.36
    libra = qntReal/6.21
    print(f'Com esse valor de R${qntReal} é possível comprar: ')
    print(f'${dEua:.2f} dólares americanos \n${pArg:.2f} pesos argentinos \nA${dAus:.2f} dólares australianos')
    print(f'C${dCan:.2f} dólares canadenses \nFr{fSui:.2f} francos suiços \n€{euro:.2f} euros \n£{libra:.2f} libras')
conversor()
'''

#2 -- aluguel de carro 
'''
print('** VALOR DE ALUGUEL DE CARRO **')
km = float(input('Digite os KM percorridos: '))
dias = int(input('Dias alugados: '))
valor = (dias * 80) + (km * 0.2)
print(f'O valor a ser pago pelo aluguel é de R${valor}.')
'''

#3 -- salário
'''
print('=-=-= AUMENTO DE SALÁRIO =-=-=')
salario = float(input('Digite o salário do funcionário: '))
if salario <= 1000:
    nsal = (salario) + (salario*0.2)
elif salario > 1000 and salario <= 2800:
    nsal = (salario) + (salario*0.1)
else:
    nsal = (salario) + (salario*0.05)
print(f'O novo salário do funcionário é de R${nsal}')
'''

#4 -- apenas números

def leiaInt():
    try:
        num = int(input('Digite um número: '))
        print(f'Número {num} cadastrado com sucesso!')
    except ValueError:
        print('ERRO! Apenas números.')
leiaInt()