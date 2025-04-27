# AI-activity-module-1


## **Resumo da Atividade**
**Tema**: Agentes coletores de recursos em um planeta desconhecido  
**Objetivo**:  
- Coletar recursos para construir uma base funcional.
- Maximizar a eficiência e terminar antes de uma tempestade de radiação.

**Data de Entrega**:  
🗓️ **Terça-feira, 26/11/2024**

**Requisitos principais**:  
✅ Programar diferentes tipos de agentes.  
✅ Simular o ambiente em grids variados.  
✅ Avaliar o desempenho dos agentes.  
✅ Implementar comunicação entre eles.  
✅ Preferência para usar **Python**.

---

## **Descrição do Ambiente**
- **Grid 2D**: representa o planeta.
- **Obstáculos**: montanhas, rios (bloqueiam o movimento).
- **Base Inicial**: onde os agentes entregam os recursos coletados.
- **Recursos**:
  - **Cristais Energéticos** (pequenos, valor 10, carregados por 1 agente)
  - **Blocos de Metal Raro** (médios, valor 20, carregados por 1 agente)
  - **Estruturas Antigas** (grandes, valor 50, precisam de 2 agentes)

---

## **Descrição dos Agentes**
| Agente                     | Comportamento |
|-----------------------------|---------------|
| Reativo Simples             | Move aleatório; coleta Cristais. |
| Baseado em Estado           | Evita áreas já exploradas; usa memória. |
| Baseado em Objetivos        | Planeja rotas até os recursos conhecidos. |
| Cooperativo (Baseado em Utilidade) | Coopera para levar Estruturas Antigas. |
| BDI (Belief-Desire-Intention) | Atualiza mapa de recursos com informações de todos; maximiza coleta total. |

---

## **Tarefas a Implementar**
- [ ] Programar lógica de movimentação, coleta e entrega de cada agente.
- [ ] Definir ações (mover, pegar recurso, entregar recurso, comunicar) e percepções (ver recurso próximo, obstáculos, outros agentes).
- [ ] Simular diferentes grids:
  - Mudança de tamanho (ex.: 10x10, 20x20, etc.)
  - Mudança na quantidade e distribuição de recursos.
- [ ] Avaliar:
  - **Desempenho individual**: quanto cada agente coleta.
  - **Desempenho em equipe**: total de recursos e valor utilitário.
- [ ] Implementar **comunicação** entre agentes (especialmente importante para Cooperativo e BDI).

---

## **Ideias Extras para Melhorar**
- Mostrar o grid visualmente (com `matplotlib` ou até `pygame`).
- Registrar a movimentação dos agentes (log).
- Gravar estatísticas finais (tempo total, utilidade total, recursos coletados).
