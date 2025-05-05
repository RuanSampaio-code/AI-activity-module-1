import random
import time

TAMANHO = 8
CICLOS_TEMPESTADE = 20

VALORES_RECURSOS = {
    'C': 10,  # Cristais
    'M': 20,  # Metal raro
    'E': 50   # Estrutura antiga (ignorada por 1 agente)
}

RECURSOS_POSSIVEIS = ['C', 'M', 'E', '.']

def gerar_ambiente():
    ambiente = []
    for _ in range(TAMANHO):
        linha = []
        for _ in range(TAMANHO):
            # Espalhar recursos com probabilidade
            recurso = random.choices(RECURSOS_POSSIVEIS, weights=[0.2, 0.15, 0.1, 0.55])[0]
            linha.append(recurso)
        ambiente.append(linha)
    return ambiente

def imprimir_ambiente(ambiente, pos):
    for i in range(TAMANHO):
        linha = ''
        for j in range(TAMANHO):
            if (i, j) == pos:
                linha += 'A '  # Agente
            else:
                linha += ambiente[i][j] + ' '
        print(linha)
    print()

def mover_agente(pos):
    direcoes = [(0,1), (0,-1), (1,0), (-1,0)]
    dx, dy = random.choice(direcoes)
    novo_x = max(0, min(TAMANHO-1, pos[0] + dx))
    novo_y = max(0, min(TAMANHO-1, pos[1] + dy))
    return (novo_x, novo_y)

def coletar_recurso(ambiente, pos):
    x, y = pos
    recurso = ambiente[x][y]
    if recurso in ['C', 'M']:
        valor = VALORES_RECURSOS[recurso]
        ambiente[x][y] = '.'  # remove recurso
        return valor
    return 0

def executar_simulacao():
    ambiente = gerar_ambiente()
    pos_agente = (random.randint(0, TAMANHO-1), random.randint(0, TAMANHO-1))
    pontos = 0

    print("🌌 Iniciando missão de coleta!")
    print("Legenda: C=Cristal, M=Metal, E=Estrutura, .=vazio, A=Agente\n")
    
    for ciclo in range(CICLOS_TEMPESTADE):
        print(f"🌪️ Ciclo {ciclo+1}/{CICLOS_TEMPESTADE}")
        imprimir_ambiente(ambiente, pos_agente)
        
        pontos += coletar_recurso(ambiente, pos_agente)
        print(f"🎯 Pontuação atual: {pontos}")
        
        pos_agente = mover_agente(pos_agente)
        time.sleep(0.5)  # pausa para simular o tempo

    print("⚠️ Tempestade de radiação! Fim da missão!")
    print(f"✅ Pontuação final: {pontos} pontos")

executar_simulacao()
