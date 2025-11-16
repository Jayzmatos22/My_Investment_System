
<div align="center">

<h1>MY INVESTMENT SYSTEM</h1>

<p>
<img src="https://img.shields.io/badge/Python-3.10+-blue">
<img src="https://img.shields.io/badge/Status-Ativo-success">
<img src="https://img.shields.io/badge/Versão-1.0-blueviolet">
<img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

</div>

---

## SOBRE O SISTEMA

Um sistema completo desenvolvido em Python, contendo:

🔐 Login + criação e validação de usuário  
📝 CRUD de informações pessoais  
📊 Mini-simulador financeiro  
✔️ Sistema modular de validações  
🖥️ Menu interativo no terminal  
💬 Estrutura totalmente escalável e refatorada

🧩 Funcionalidades Principais
🔐 Autenticação

  •--->Criação de usuário

  •--->Login com verificação direta

  •--->Bloqueio ou mensagens de erro configuradas
<br><br><br><br>
📝 CRUD de Dados

•--->Usuário pode criar, visualizar, atualizar e remover informações pessoais.

•--->O sistema usa validações específicas (nome, idade, sexo, numéricos etc.), garantindo dados consistentes.
<br><br><br><br>
📊 Mini Simulador Financeiro

•--->Cálculo automático com base no tipo de métrica escolhida pelo usuário.
Inclui:

•--->Formatação de saída

•--->Erros tratados

•--->Ajuste automático de tipo numérico
<br><br><br><br>
🧱 Arquitetura do Sistema

•--->O projeto é dividido em módulos como:

•--->Validações

•--->Entradas seguras

•--->Sistema de menu

•--->Manipulação de dicionário de dados

•--->Simulações diversas

•--->Essa estrutura permite:

•--->Fácil expansão

•--->Adição de novos módulos

•--->Alterações isoladas sem quebrar o sistema
<br><br><br><br>

🧹 Tratamento de Erros e Entrada

Inclui:

•--->Loops de segurança

•--->Proteção contra entradas vazias

•--->Tratamento de ValueError

•--->Sistema completo de feedback colorido no termina
<br><br><br><br>
📂 **Estrutura Geral**

```
MyInvestmentSystem/
├── validações (funções)
│   ├── validar_nome
│   ├── validar_email
│   ├── validar_senha
│   ├── validar_codigo_numerico
│   ├── validar_flutuante
│   ├── validar_inteiro
│   └── validar_rg
├── sistema de login
│   ├── criar conta
│   ├── acessar conta
│   ├── recuperar email
│   ├── recuperar senha
│   └── atualizar credenciais
├── módulo de investimentos
│   ├── entrada de dados
│   ├── cálculos
│   └── relatórios
└── design ANSI (cores e formatação)
