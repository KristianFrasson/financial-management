# Levantamento de Requisitos

**Projeto:** Controle Financeiro Pessoal  
**Versão:** 1.0  
**Data:** 10/11/2024  
**Autor:** Kristian

## 1. Introdução

### 1.1 Visão Geral

Aplicativo web desenvolvido para gestão financeira pessoal, com o objetivo de aprimorar habilidades de programação e adicionar ao portfólio profissional.

### 1.2 Objetivos

- Melhorar a gestão e controle financeiro pessoal.
- Aprender e aplicar tecnologias web modernas (Flask e React).
- Criar um repositório para apresentação em entrevistas de emprego.

## 2. Requisitos Funcionais

### 2.1 Sistema de Autenticação

- O sistema deve permitir login seguro utilizando JWT.
- Deve haver controle de sessões e armazenamento seguro de credenciais.

### 2.2 Dashboard Principal

- Exibir faturas do mês atual.
- Mostrar entradas de capital (salário, investimentos, rendas extras).
- Apresentar saldo do mês calculado (entradas - saídas).
- Exibir gastos previstos (gastos fixos + parcelas de cartões de crédito).
- Mostrar total de despesas fixas para o mês.

### 2.3 Análises Gráficas

- Gráficos detalhados das faturas do cartão de crédito.
- Análise de categorias de gastos realizados no cartão.
- Gráficos de gastos fixos e renda mensal.

### 2.4 Área de Cadastro

- Cadastro de cartões de crédito com informações detalhadas (limite, datas de vencimento e fechamento).
- Registro de compras com opções de parcelamento e categorias.
- Cadastro de entradas de capital com opção de recorrência (fixa ou variável).
- Cadastro de gastos fixos com nome, categoria e valor.

## 3. Requisitos Não Funcionais

### 3.1 Desempenho

- O sistema deve responder rapidamente às interações do usuário.

### 3.2 Segurança

- Utilizar padrões de segurança para proteger os dados financeiros.
- Armazenar chaves e segredos em variáveis de ambiente.

### 3.3 Usabilidade

- Interface intuitiva e responsiva.
- Navegação fácil entre as funcionalidades.

### 3.4 Escalabilidade

- Estrutura modular que permite futuras expansões e adição de novas funcionalidades.

## 4. Tecnologias

- **Backend:** Python (Flask)
- **Frontend:** React.js
- **Banco de Dados:** SQLite (para simplificar a inicialização)

## 5. Estrutura de Diretórios

```
personal-financial-management-system/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── venv/
│   └── ... (outros arquivos do backend)
├── frontend/
│   ├── package.json
│   ├── src/
│   │   └── App.js
│   └── ... (outros arquivos do frontend)
├── docs/
│   └── software_requirements.md
└── ... (outros arquivos e diretórios)
```

## 6. Cronograma

- **Início do Projeto:** 27/04/2024
- **Implementação do Backend:** 10/05/2024
- **Implementação do Frontend:** 20/05/2024
- **Testes e Integração:** 30/05/2024
- **Lançamento do Sistema:** 01/06/2024

## 7. Considerações Finais

Este projeto é uma aplicação pessoal focada no aprendizado e no desenvolvimento de habilidades práticas em programação web. As funcionalidades podem ser expandidas conforme a necessidade e interesse.
