
import sys
import streamlit as st
import pandas as pd

sys.path.append('src/')

from api.model.pipeline import Pipeline

model = Pipeline().carrega_pipeline('src/api/MachineLearning/models/churn_modelling_pipeline_rf.pkl')

st.title('Modelo de Predição de Churn')

credit_score = st.number_input('Qual o score de crédito?', step=1, format='%d', max_value=1000)
geography = st.selectbox("Qual o país?", options=['França','Espanha', 'Alemanha'])
gender = st.selectbox("Qual o gênero?", options=['Feminino', 'Masculino'])
age = st.number_input('Qual a idade?', step=1, format='%d')
tenure = st.number_input('Qual o tempo de relacionamento com o banco?', step=1, format='%d')
balance = st.number_input('Qual o saldo da conta?')
num_of_products = st.number_input('Qual a quantidade de produtos no banco?', step=1, format='%d')
has_credit_card = st.selectbox("Tem cartão de crédito?", options=['sim','não'])
is_active_member = st.selectbox("É um cliente ativo?", options=['sim','não'])
estimated_salary = st.number_input('Qual o salário?')


#Transformações dos valores recebidos

# Mapeamentos para transformar inputs
geography_map = {'França': 'France', 'Espanha': 'Spain', 'Alemanha': 'Germany'}
gender_map = {'Feminino': 'Female', 'Masculino': 'Male'}
binary_map = {'sim': 1, 'não': 0}

# Aplicando as transformações
geography_en = geography_map[geography]
gender_en = gender_map[gender]
has_credit_card_boolean = binary_map[has_credit_card]
is_active_member_boolean = binary_map[is_active_member]

# Construção dicionário de input
input= {
        'CreditScore':  [credit_score],
        'Geography': [geography_en],
        'Gender': [gender_en],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_credit_card_boolean],
        'IsActiveMember': [is_active_member_boolean],
        'EstimatedSalary': [estimated_salary],
}

# Nomes das colunas (features)
colunas = ['CreditScore','Geography','Gender','Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']

# Convertendo o dicionário em um DataFrame
entrada = pd.DataFrame(input, columns=colunas)


if st.button('Fazer predição de churn'):
    with st.spinner('Calculando predição...'):
        prediction = model.predict(entrada)

    if prediction[0] == 1:
        st.error('O cliente tem **RISCO** de churn', icon="⚠️")
    else:
        st.success('Não há **RISCO** de churn para o cliente', icon="✅")

