Esse projeto é uma dashboard climática a partir da API do openweather 

***O que é necessário instalar*** 
- Versão estável atualizada do Python a partir do 3
- requirements.txt, comando: pip install -r requirements.txt
*** O que é preciso ter?***
- Uma key da API da OpenWeather(Gratuita)
- VSCode
### Como Rodar
No terminal, digite:
python -m streamlit run app.py
### Usar o Dashboard
1. O navegador abrirá automaticamente (geralmente em http://localhost:8501).
2. Na barra lateral esquerda, digite sua **Chave de API** (API Key).
3. Digite o nome da cidade desejada no campo principal e pressione Enter.

##  Estrutura do Projeto
* app.py`: Interface gráfica (Frontend).
* src/models.py: Classes e estrutura de dados (POO).
* src/chave_api.py: Conexão com a API OpenWeather.
* src/processamento.py: Tratamento de dados com Pandas e Lambda.
