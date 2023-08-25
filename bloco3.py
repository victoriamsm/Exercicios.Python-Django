#1 -- médias
'''
lista_medias = []
alunos = 0
totMed = 0
# # # parte 1 # # #
while alunos < 10:
    print(f'ALUNO {alunos+1}') 
    notas = [] 

    for c in range(0, 4):
        notas.append(float(input(f'Nota {c+1}: ')))

    lista_medias.append(sum(notas) / len(notas))
    print(f'Sua média é {lista_medias[alunos]} \n {"=-"*10}')
    alunos += 1

### parte 3 ###

for i in lista_medias:
    if i >= 7:
        totMed += 1 
print(f'Ao todo são {totMed} alunos acima da média!')
'''

#2 -- inverso
'''
nome = str(input('Digite seu nome para vê-lo AO CONTRÁRIO: ')).strip().upper()
print(f'Seu nome {nome} de forma inversa é {nome[::-1]}!')
'''

#3 -- dicionário 
'''
dicionario = {'nome':'Maria','idade':40,'profissão':"",'endereço':[]}

for k, v in dicionario.items():
    if not v:
        print(f'{k} -- [VAZIO] --> False')
    else:
        print(f'{k} -- {v} --> True')
'''

#4 -- investigação

lista_perg = ['Telefonou para vítima?','Esteve no local do crime?', 
              'Mora perto da vítima?', 'Devia para vítima?',
                'Já trabalhou com a vítima?']
resp = []
totS = 0
print('** INVESTIGAÇÃO DO CASO XXZ **')
for i in range(0,len(lista_perg)):
    print(lista_perg[i],end='')
    resp.append(input(' [S/N] '))
    if resp[i] in 'Ss':
        totS += 1
if totS < 2: 
    print('Status: INOCENTE')
elif totS == 2:
    print('Status: SUSPEITO')
elif totS <= 4:
    print('Status: CÚMPLICE')
elif totS == 5:
    print('Status: ASSASSINO')
