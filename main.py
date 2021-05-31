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
