from abc import ABC, abstractmethod

class Cliente():

    def __init__(self, nome, telefone, renda):
        self.nome = nome
        self._telefone = telefone
        self._renda_mensal = renda

class Conta_corrente(ABC):

    def __init__(self, saldo):
        self._saldo = saldo
        self._operacao = []
    
    @abstractmethod
    def sacar(self, valor): #Operacao1 
        pass

    @abstractmethod
    def depositar(self, valor): #Operacao2
        pass
    
    def obter_operacao(self):
        return self._operacao

    def mostrar_operacao(self):
        for operacao in self._operacao:
            print(operacao)

class Conta_Mulher(Conta_corrente):
    def __init__(self, cliente):
        super().__init__(cliente._renda_mensal)
        self.clientes = [cliente]
        self.cheque_especial = -cliente._renda_mensal
    
    def sacar(self, valor):
        if self._saldo - valor >= self.cheque_especial: #se o saldo - valor for menor ou igual ao cheque esp
            self._saldo -= valor
            self._operacao.append(f'Saque: {valor}')
        else:
            print('Saldo insuficiente.')
    
    def depositar(self, valor):
        self._saldo += valor
        self._operacao.append(f'Depósito: {valor}')

class Conta_Homem(Conta_corrente):
    def __init__(self, cliente):
        super().__init__(0) #homem não tem cheque especial
        self.clientes =[cliente]
    
    def sacar(self, valor):
        if self._saldo - valor >= 0:
            self._saldo -= valor
            self._operacao.append(f'Saque: {valor}')
        else:
            print('Saldo insuficiente')
    
    def depositar(self, valor):
        self._saldo += valor
        self._operacao.append(f'Depósito: {valor}')


cliente_mulher = Cliente('Luíza', '93823-8455', 4000)
conta_mulher = Conta_Mulher(cliente_mulher)
print(f'Saldo da conta de {cliente_mulher.nome}: {conta_mulher._saldo}')
conta_mulher.sacar(8100) #Só consegue sacar até 8000, no caso em questão
print(f'Saldo da conta de {cliente_mulher.nome}: {conta_mulher._saldo}') #continua o mesmo
conta_mulher.depositar(8300)

print(f'Saldo da conta de {cliente_mulher.nome}: {conta_mulher._saldo}')

print(f"Operações da conta de {cliente_mulher.nome}:")
conta_mulher.mostrar_operacao()
print('--'*20)

cliente_mulher1 = Cliente('Maria', '92823-1234', 8000)
conta_mulher1 = Conta_Mulher(cliente_mulher1)
print(f'Conta de {cliente_mulher1.nome} tem R${conta_mulher1._saldo} de saldo!')
print(f"Operações da conta de {cliente_mulher1.nome}:")
conta_mulher1.mostrar_operacao()
print('Recebeu salário')

print('--'*20)

cliente_homem = Cliente('Carlos','91234-5678', 3200)
conta_homem = Conta_Homem(cliente_homem)

conta_homem.depositar(700)
print(f'Conta de {cliente_homem.nome} tem R${conta_homem._saldo} de saldo!')
conta_homem.sacar(350)
print(f"Operações da conta de {cliente_homem.nome}:")
conta_homem.mostrar_operacao()
print(f'Conta de {cliente_homem.nome} tem R${conta_homem._saldo} de saldo!')