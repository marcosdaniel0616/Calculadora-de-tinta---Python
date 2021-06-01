class Calculadora:
    __area_paredes: float
    __area_teto: float

    def calcular_area_paredes(self, comodo):
        self.area_paredes = 2 * (comodo.largura + comodo.profundidade) * comodo.altura
        return self.area_paredes

    def calcular_area_teto(self, comodo):
        self.area_teto = comodo.largura * comodo.profundidade
        return self.area_teto

    def calcular_litragem_necessaria(self):
        if self.area_paredes <= 0 or self.area_teto <= 0:
            print('Não é possível calcular a litragem com os valores informados!')
            exit()
        else:
            return (self.area_paredes + self.area_teto) / 10


