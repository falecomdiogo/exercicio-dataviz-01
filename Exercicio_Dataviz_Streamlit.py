#!/usr/bin/env python
# coding: utf-8

#%%
# #   Exercício de DataViz Asimov Academy
# ### Criação de dashboard simples utilizando Pandas, Streamlit e Plotly Express.

#%%
# Instalando os pacotes necessários

# !pip install pandas
# !pip install streamlit
# !pip install plotly


#%%

# importando os pacotes

import pandas as pd
import streamlit as st
import plotly.express as px


#%%

# definindo o layout da página para wide

st.set_page_config(layout='wide')

# adicionando um título para a página

st.subheader('Diogo Moreira Pinto')
st.title('Exercício de DataViz - Asimov Academy')


#%%

# fazendo a leitura do DataSet "Supermarket Sales"
# criando o dataframe e lendo as 5 primeiras linhas

df = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')
df.head(5)


#%%

# deletando possíveis duplicatas

df.drop_duplicates()


#%%

# convertendo a coluna Date para datetime do Pandas

df.Date = pd.to_datetime(df.Date)
df = df.sort_values('Date')
df.info()


#%%

# adicionando uma coluna de meses por ano em formato
# string para podermos obter a visualização mensal

df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))


#%%

# criando uma sidebar do Streamlit para filtrar os meses

st.sidebar.subheader('Selecione o período:')
month = st.sidebar.selectbox('Mês', df['Month'].unique())

# filtrando o df

df_filter = df[df['Month'] == month]


#%%

# criando as colunas do layout da pág. no Streamlit

col1, col2 = st.columns(2) # duas colunas na parte superior
col3, col4, col5 = st.columns(3) # três colunas na parte inferior da página

#%%
# ## Criando os gráficos com Plotly Express

#%%

# gráfico de faturamento por unidade

fig_date = px.bar(df_filter, x='Date', y='Total', color='City', title='Faturamento por unidade')
col1.plotly_chart(fig_date, use_container_width=True) # endereçando o gráfico à coluna 1 dá pág.


#%%

# gráfico de faturamento por tipo de produto

fig_prod = px.bar(df_filter, x='Date', y='Product line', color='City', title='Faturamento por tipo de produto', orientation='h')
col2.plotly_chart(fig_prod, use_container_width=True) # endereçando o gráfico à coluna 2 dá pág.


#%%

# gráfico de faturamento por filial

df_city = df_filter.groupby('City')[['Total']].sum().reset_index()
fig_city = px.bar(df_city, x='City', y='Total', title='Faturamento por filial')
col3.plotly_chart(fig_city, use_container_width=True) # endereçando o gráfico à coluna 3 dá pág.


#%%

# gráfico de faturamento por tipo de pagamento

fig_pay = px.pie(df_filter, values='Total', names='Payment', title='Faturamento por tipo de pagamento')
col4.plotly_chart(fig_pay, use_container_width=True) # endereçando o gráfico à coluna 4 dá pág.


#%%

# gráfico de avaliação

df_rank = df_filter.groupby('City')[['Rating']].mean().reset_index()
fig_rank = px.bar(df_rank, x='Rating', y='City', title='Avaliação')
col5.plotly_chart(fig_rank, use_container_width=True) # endereçando o gráfico à coluna 5 dá pág.

#%%
# # FIM
