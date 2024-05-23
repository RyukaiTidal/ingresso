class Ingresso():
    def __init__(self, valor):
        self.valor =  valor

    def imprimeValor(self):
        print(f"O ingresso Normal custa R${self.valor}")

class IngressoVip(Ingresso):
    def __init__(self,valor,amais):
        super().__init__(valor)
        self.valoradicional = self.valor + amais

    def imprimeValor(self):
        print(f"O ingresso VIP custa R${self.valoradicional}")
