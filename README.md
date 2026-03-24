#  Pong Refatorado com Pygame

## Descrição
Este projeto é uma implementação do clássico jogo Pong utilizando **Python** e **Pygame**, com foco em refatoração de código e aplicação de boas práticas de engenharia de software.

O objetivo principal foi melhorar a organização, legibilidade e manutenção do código, aplicando princípios como **SOLID**, abstração e separação de responsabilidades.

---

## Objetivo
Desenvolver uma versão modular e escalável do Pong, permitindo fácil manutenção e expansão do sistema.

---

## Arquitetura

O projeto foi estruturado em classes com responsabilidades bem definidas:

### Game
- Controla o loop principal
- Gerencia eventos
- Atualiza o estado do jogo
- Controla a pontuação

### raquete
- Representa as raquetes
- Controla movimentação
- Garante limites da tela

###  Bola
Controla movimento da bola
Gerencia colisões
Realiza reset de posição

###  Menu
Exibe o menu inicial
Captura interação do usuário
Inicia o jogo

---

## Fluxo do Sistema

1. O jogo inicia pelo menu principal
2. O usuário pressiona **ESPAÇO**
3. O jogo começa
4. Durante o jogo:
   Entrada do jogador é processada
   Bola se movimenta
   Colisões são detectadas
    Pontuação é atualizada
5. O loop continua até o usuário sair

---

## Princípios SOLID

### Single Responsibility
Cada classe possui uma única responsabilidade.

### Open/Closed
O sistema permite extensão sem modificar código existente.

### Liskov Substitution
As classes podem ser estendidas sem quebrar o sistema.

### Interface Segregation
Métodos específicos para cada necessidade.

### Dependency Inversion
Uso de abstrações ao invés de dependências diretas.

---

## Melhorias Aplicadas

Separação de responsabilidades
Criação de classes específicas
Padronização de nomes
Redução de código duplicado
Organização do código em métodos
Uso de constantes
Inclusão de comentários e docstrings

---

## Legibilidade

Nomes claros e descritivos
Código modular
Estrutura organizada
Fácil entendimento e manutenção

---

## Possíveis Melhorias Futuras

Multiplayer local (2 jogadores)
Sistema de níveis/dificuldade
Aumento progressivo da velocidade da bola
Adição de sons e efeitos visuais
Menu interativo com opções

---

## Tecnologias Utilizadas

- Python
- Pygame

---

## Como Executar

1. Instale o Pygame:
```bash
pip install pygame