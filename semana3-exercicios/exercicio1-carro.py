class Carro():
    def __init__(self, cor, modelo): # MÉTODO / ATRIBUTO
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
        self.velocidade_max = 200
        self.velocidade_min = 0

    def ligar(self):  #COMPORTAMENTO
        self.ligado = True 

    def desligar(self):
        self.ligado = False
        self.velocidade = 0.0

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
        ligado_str = "ligado" if self.ligado == True else "desligado"
        return f'O carro da cor {self.cor} e modelo {self.modelo} está {ligado_str} com a velocidade atual de {self.velocidade}KM!'

carro1 = Carro("Azul", "Evoque")

carro1.ligar()
print(carro1)
print('-='*15)


print(f'Acelerando carro: ',end='')
for i in range(8):
    carro1.acelerar()
    print(f'{carro1.velocidade}...',end='')
print(' [VELOCIDADE MÁXIMA DA VIA!]')
print(carro1)
print('-='*15)

print(f'Desacelerando o carro: ',end='')
for i in range(8):
    carro1.desacelerar()
    print(f'{carro1.velocidade}...',end='')
print(' [PAROU!]')

carro1.desligar()

print('Carro: ', carro1)
