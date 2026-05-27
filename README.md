# 📊 Análise de Leads Imobiliários

Script Python para análise de leads de uma imobiliária, com geração de relatório em Excel e gráficos automáticos.

## O que faz

- Carrega e organiza a base de leads
- Calcula taxa de conversão geral e por canal de origem
- Gera gráficos de distribuição de leads e status
- Exporta relatório completo em `.xlsx` com duas abas

## Tecnologias

- `pandas` — manipulação e análise dos dados
- `matplotlib` — geração dos gráficos
- `openpyxl` — exportação para Excel

## Como rodar

```bash
pip install pandas matplotlib openpyxl
python analise_leads.py
```

Os arquivos gerados ficam na pasta `outputs/`.

## Contexto

Desenvolvido com base em experiência prática com gestão de leads em imobiliária, onde acompanhamento de conversão e origem dos contatos era parte do trabalho diário.