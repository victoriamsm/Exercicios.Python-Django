def calcular_media(valores):
    if not valores:
        return 0  # Retorna 0 se a lista estiver vazia para evitar divisão por zero
    tamanho = len(valores)
    soma = sum(valores)
    media = soma / tamanho
    return media

valores = []
while True:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ') #string
    if valor.lower() == 'ok':
        break  # Encerra o loop se o usuário digitar 'ok'
    try:
        valor = float(valor)
        valores.append(valor)
    except ValueError:
        print('Digite um número válido.')

media = calcular_media(valores)
print(f'A média calculada para os valores {valores} foi de {media:.2f}')
