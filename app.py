import streamlit as st, pandas as pd 
from src.chave_api import ClienteAPI 
from src.processamento import processar_previsao_5_dias, calcular_medias_diarias 

st.set_page_config(page_title="Dashboard do Tempo", page_icon="🌤️", layout="wide")

with st.sidebar:
    st.header("Autentificação da API")
    chave_api = st.text_input("Chave da API:", type="password")
    st.info("Pressione enter após inserir a cidade") 

st.title("Monitoramento Climático em Tempo Real")
st.markdown("Esse Dashboard foi feito a partir dos dados da API OpenWeatherMap.")

cidade_input = st.text_input("Digite o nome da cidade:", " ")
if cidade_input and chave_api:
    api = ClienteAPI(chave_api)
    cidade = api.buscar_cidade(cidade_input)
    if cidade: 
        clima = api.get_clima_atual(cidade.lat, cidade.lon)
        poluicao = api.get_poluicao_ar(cidade.lat, cidade.lon) 

        st.subheader(f"Clima Atual em {cidade.nome} ({cidade.pais})")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Temperatura", f"{clima.temp}°C")
        col2.metric("Sensação Térmica", f"{clima.sens_termica}°C")
        col3.metric("Umidade", f"{clima.umidade}%")

        if poluicao:
            col4.metric("Qualidade do AR", f"{poluicao.aqi}/5")
        
        st.markdown(f"**Condição:** {clima.descricao.title()}")
        st.divider()

        st.subheader("Previsão para os Próximos 5 dias")
        previsao_lista = api.get_previsao_5dias(cidade.lat, cidade.lon)
        if previsao_lista: 
            df_bruto = processar_previsao_5_dias(previsao_lista)
            df_medias = calcular_medias_diarias(df_bruto)

            tab1, tab2 = st.tabs(["Gráfico de Temperatura", "Dados Detalhados"])
            with tab1: 
                st.markdown("### Evolução da Temperatura Média Diária")
                st.line_chart(df_medias, x="Data", y="Temp Média (°C)") 
            with tab2:
                st.markdown("Tabela de Previsão de 3 em 3 horas")
                st.dataframe(df_bruto, use_container_width=True)
        else:
            st.error("Cidade não encontrada. Verifique o nome.")
    elif not chave_api:
        st.warning("Por favor, insira a chave da API na barra lateral.")