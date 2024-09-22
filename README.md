# Predicao-churn-clientes-bancarios

Projeto da sprint de **Qualidade de Software, Segurança e Sistemas Inteligentes** do [curso de pós graduação de Engenharia de Sofware da PUC Rio](https://especializacao.ccec.puc-rio.br/especializacao/engenharia-de-software).

## Objetivo do projeto
Desenvolver o treinamento de um modelo de classificação de machine learning e integrá-lo com uma aplicação fullstack, que possibilite a entrada de novos dados no frontend para que o modelo de classificação faça a predição da classe de saida e exiba o resultado na tela.

## Como executar
Para executar o projeto, siga os passos:
1. Clone o repositório
2. Instale a lib do poetry usando o pip
```bash
pip install poetry
```

> É fortemente indicado o uso de ambientes virtuais do poetry, pois segue a orientação prevista na [PEP 621](https://peps.python.org/pep-0621/) 
3. Faça a instalação das dependências listadas no [arquivo pyproject.toml](https://github.com/camilaccb/BuddyConnect-Backend/blob/main/pyproject.toml):

```bash
poetry install
```
4. Ative o ambiente virtual. Caso tenha alguma dúvida consultar a seguinte [documentação](https://python-poetry.org/docs/basic-usage/#:~:text=shell%0Awhich%20python-,Activating%20the%20virtual%20environment,-The%20easiest%20way)

```bash
poetry shell
```

5. Execute a aplicação

```bash
(env)$ streamlit run src/front/page.py
```

