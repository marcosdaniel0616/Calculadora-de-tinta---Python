"""
nome_da_variável: float -> o nome disso é typehint, é uma "sugestão" sobre qual o tipo da variável
"""

largura: float = float(input('Qual a largura do cômodo? '))
profundidade: float = float(input('Qual a profundidade do cômodo? '))
altura: float = 2.9  # 2.9 é o tamanho padrão de altura das construções do Brasil


print("a área das paredes é",  (2 * (largura + profundidade) * altura))
