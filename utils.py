import requests
import pandas as pd

def get_who_data(indicator_code):
    """
    Busca dados da WHO API para o indicador especificado.
    
    Args:
        indicator_code (str): Código do indicador (ex: 'MMR_100000_LB')
    
    Returns:
        pd.DataFrame: Dados retornados da API como DataFrame
    """
    url = f"https://ghoapi.azureedge.net/api/{indicator_code}"
    response = requests.get(url)
    response.raise_for_status()
    return pd.json_normalize(response.json()['value'])
