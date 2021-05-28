"""
nome_da_variável: float -> o nome disso é typehint, é uma "sugestão" sobre qual o tipo da variável

Type hint no Python:
Type Hint é um mecanismo do Python 3 através do qual podemos dar uma dica
sobre o tipo de uma variável.

area_parede : float = 2.5
Embora seja possível com esse recurso alertar o leitor do código
sobre o tipo de dado que esperamos que a variável receba,
Type Hint não altera o modelo de tipagem do Python, que é dinâmico.
"""

largura: float = float(input('Qual a largura do cômodo? '))
profundidade: float = float(input('Qual a profundidade do cômodo? '))
altura: float = 2.9  # 2.9 é o tamanho padrão de altura das construções do Brasil

area_paredes: float = (2 * (largura + profundidade) * altura)

print("a área das paredes é",  area_paredes)

area_teto: float = largura * profundidade

print(
    'A área do teto é:',
    area_teto
)

print(
    'A litragem de tinta é necessária:',
    ((area_paredes + area_teto) / 10)
)
