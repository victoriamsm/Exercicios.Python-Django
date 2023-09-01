class Carro():
    def __init__(self): # MÉTODO / ATRIBUTO
        self.ligado = False
        self.cor = 'Azul'
        self.modelo = 'Evoque SUV'
        self.velocidade = 0
        self.velocidade_max = 230
        self.velocidade_min = 0
    def ligar(self):  #COMPORTAMENTO
        self.ligado = True 
    def desligar(self):
        self.ligado = False
    def acelerar(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10
    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10
    def __str__(self) -> str:
        return f'-Ligado: {self.ligado} -Cor: {self.cor} -Modelo: {self.modelo} Velocidade atual: {self.velocidade}'

carro1 = Carro()

carro1.ligar()
print(f'O carro está ligado? {carro1.ligado}')

print(f'Acelerando carro: ',end='')
for i in range(8):
    carro1.acelerar()
    print(f'{carro1.velocidade}...',end='')
print(' [VELOCIDADE MÁXIMA DA VIA!]')

print(f'Desacelerando o carro: ',end='')
for i in range(8):
    carro1.desacelerar()
    print(f'{carro1.velocidade}...',end='')
print(' [PAROU!]')

carro1.desligar()


print('Carro: ', carro1)
