from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    largura=input('Qual a largura do cômodo? '),
    profundidade=input('Qual a profundidade do cômodo? ')
)

print("a área das paredes é",
      calc.calcular_area_paredes(comodo.largura, comodo.profundidade, comodo.altura))

print(
    'A área do teto é:',
    calc.calcular_area_teto(comodo.largura, comodo.profundidade)
)

print(
    'A litragem de tinta é necessária:',
    (calc.calcular_litragem_necessaria())
)
