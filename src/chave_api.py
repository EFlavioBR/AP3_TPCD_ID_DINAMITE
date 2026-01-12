import requests 
from src.models import Cidade, ClimaAtual, Previsao, Poluicao 

class ClienteAPI: 
    def __init__(self, api_key: str):
        self.api_key = api_key 
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.geo_url = "http://api.openweathermap.org/geo/1.0"

    def get_request(self, url: str, params: dict): 
        try: 
            params['appid'] = self.api_key
            resposta_rqst = requests.get(url, params=params)
            resposta_rqst.raise_for_status() 
            return resposta_rqst.json() 
        except requests.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None 
        
    def buscar_cidade(self, nome_cidade: str, pais: str = "BR") -> Cidade | None: 
        url = f"{self.geo_url}/direct"
        params = {"q": nome_cidade, "limit": 1}

        data = self.get_request(url, params)
        if data and len(data) > 0:
            return Cidade.info_api_data(data[0])
        return None
    
    def get_clima_atual(self, lat: float, lon: float) -> ClimaAtual | None: 
        url = f"{self.base_url}/weather"
        params = {"lat": lat, "lon": lon, "units": "metric", "lang": "pt_br"} 

        data = self.get_request(url, params)
        if data:
            return ClimaAtual.info_api_data(data)
        return None

    def get_previsao_5dias(self, lat: float, lon: float) -> list[Previsao] | None: 
        url = f"{self.base_url}/forecast"
        params = {"lat": lat, "lon": lon, "units": "metric", "lang": "pt_br"} 

        data = self.get_request(url, params) 
        lista_previsoes = []

        if data and "list" in data: 
            for item in data["list"]: 
                previsao = Previsao.info_api_data(item)
                lista_previsoes.append(previsao)
        
        return lista_previsoes

    def get_poluicao_ar(self, lat: float, lon: float) -> Poluicao | None: 
        url = f"{self.base_url}/air_pollution"
        params = {"lat": lat, "lon": lon} 

        data = self.get_request(url, params)
        if data: 
            return Poluicao.info_api_data(data)
        return None 
    
        
     
            
        