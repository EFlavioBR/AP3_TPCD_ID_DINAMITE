from dataclasses import dataclass
from typing import List, Optional 

#1. Classe para representar a cidade 
@dataclass 
class Cidade: 
    nome: str 
    lat: float 
    lon: float 
    pais: str = "BR"

    @staticmethod
    def info_api_data(data: dict): 
        return Cidade(
            nome=data.get("name", "Desconhecida"), 
            lat=data.get("lat", 0.0), 
            lon=data.get("lon", 0.0), 
            pais=data.get("country", "BR")
        )

@dataclass
#2. Classe para o clima atual
class ClimaAtual: 
    temp: float 
    sens_termica: float 
    umidade: int 
    vel_vento: float 
    descricao: str 
    icone: str 

    @staticmethod
    def info_api_data(data: dict): 
        main = data.get("main", {}) 
        wind = data.get("wind", {}) 
        weather = data.get("weather", [{}])[0] 

        return ClimaAtual( 
            temp=main.get("temp", 0.0), 
            sens_termica=main.get("feels_like", 0.0), 
            umidade=main.get("humidity", 0), 
            vel_vento=wind.get("speed", 0.0), 
            descricao=weather.get("description", "N/A"), 
            icone=weather.get("icon", "01d") 
        )

#3. Classe para previsão 
@dataclass
class Previsao: 
    data_hora: str
    temp: float 
    descricao: str 
    prob_chuva: float 

    @staticmethod
    def info_api_data(data: dict): 
        weather = data.get("weather", [{}])[0] 

        return Previsao( 
            data_hora=data.get("dt_txt", ""), 
            temp=data.get("main", {}).get("temp", 0.0), 
            descricao=weather.get("description", ""), 
            prob_chuva=data.get("pop", 0.0) 
        )

#4. Poluição 
@dataclass
class Poluicao: 
    aqi: int 
    co: float 
    no2: float 
    pm2_5: float 

    @staticmethod
    def info_api_data(data: dict): 
        item = data.get("list", [{}])[0]
        componentes = item.get("components", {})
        main = item.get("main", {})
        
        return Poluicao( 
            aqi=main.get("aqi", 0), 
            co=componentes.get("co", 0.0), 
            no2=componentes.get("no2", 0.0), 
            pm2_5=componentes.get("pm2_5", 0.0) 
        ) 
