from calculadora import Calculadora

calc = Calculadora()

largura: float = float(input('Qual a largura do cômodo? '))
profundidade: float = float(input('Qual a profundidade do cômodo? '))
altura: float = 2.9  # 2.9 é o tamanho padrão de altura das construções do Brasil

# calc.area_paredes = (2 * (largura + profundidade) * altura)

print("a área das paredes é",
      calc.calcular_area_paredes(largura, profundidade, altura))

# calc.area_teto = largura * profundidade

print(
    'A área do teto é:',
    calc.calcular_area_teto(largura, profundidade)
)

print(
    'A litragem de tinta é necessária:',
    (calc.calcular_litragem_necessaria())
)
