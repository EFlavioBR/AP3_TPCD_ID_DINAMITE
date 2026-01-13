import pandas as pd 
from src.models import Previsao 

def processar_previsao_5_dias(lista_previsoes: list[Previsao]) -> pd.DataFrame:
    """
    Processa uma lista de objetos Previsao e retorna um DataFrame com as previsões dos próximos 5 dias.

    Args:
        lista_previsoes (list[Previsao]): Lista de objetos Previsao.
    """ 
    dados_formatados = list(map(lambda p: {
        "Data/Hora": p.data_hora,
        "Temperatura": p.temp,
        "Descrição": p.descricao, 
        "Chuva": p.prob_chuva * 100 
    }, lista_previsoes))

    df = pd.DataFrame(dados_formatados)
    if not df.empty:
        df['Data/Hora'] = pd.to_datetime(df['Data/Hora'])
        return df 
    
def calcular_medias_diarias(df: pd.DataFrame) -> pd.DataFrame: 
    """
    Calcula as médias diárias de temperatura e probabilidade de chuva a partir de um DataFrame de previsões horárias.

    Args:
        df (pd.DataFrame): DataFrame contendo previsões horárias com colunas "Data/Hora", "Temperatura (°C)" e "Chuva (%)".

    Returns:
        pd.DataFrame: DataFrame com médias diárias de temperatura e probabilidade de chuva.
    """ 
    if df.empty: 
        return pd.DataFrame()
    
    df_diario = df.groupby(df["Data/Hora"].dt.date)["Temperatura"].mean().reset_index()
    df_diario.columns = ["Data", "Temp Média (°C)"]
    df_diario["Temp Média (°C)"] = df_diario["Temp Média (°C)"].round(2)
    return df_diario 

