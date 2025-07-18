import re
import pandas as pd

def clean_column_names2(df):
    """
    Padroniza os nomes das colunas para snake_case, minúsculas e sem caracteres especiais.
    
    Args:
        df (pd.DataFrame): DataFrame para limpar as colunas.
        
    Returns:
        pd.DataFrame: DataFrame com colunas limpas.
    """
    def camel_to_snake(name):
        # Insere underscore antes das letras maiúsculas e transforma tudo em minúsculo
        name = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
        name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
        return name.lower()

    df.columns = (
        df.columns
        .str.strip()  # tira espaços no começo/fim (por precaução)
        .map(camel_to_snake)  # transforma CamelCase em snake_case
        .str.replace(r'[^a-z0-9_]', '', regex=True)  # remove caracteres especiais
    )
    return df



def drop_empty_columns(df):
    """
    Remove todas as colunas completamente vazias de um DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada.

    Returns:
        pd.DataFrame: DataFrame sem colunas vazias.
    """
    return df.dropna(axis=1, how='all')

def check_data_quality(df):
    """
    Exibe informações sobre o DataFrame:
    - Tipos de dados
    - Valores nulos
    - Duplicatas
    
    Args:
        df (pd.DataFrame): DataFrame para diagnosticar.
    """
    print("\n Info do DataFrame:")
    print(df.info())
    print("\n Tipos de Dados:")
    print(df.dtypes)
    print("\n Estatísticas Descritivas:")
    print(df.describe(include='all'))
    print("\n Valores Nulos por Coluna:")
    print(df.isnull().sum())
    print("\n Total de Duplicatas:")
    print(df.duplicated().sum())

def fix_column_types(df):
    """
    Corrige os tipos das colunas restantes:
    - Converte para category, datetime e int onde apropriado.
    """
    # Converte para category
    category_cols = [
        'indicator_code', 'spatial_dim_type', 'spatial_dim',
        'time_dim_type', 'parent_location_code', 'parent_location'
    ]
    for col in category_cols:
        df[col] = df[col].astype('category')
        print(f"{col}: convertido para category")
    
    # Converte para datetime
    date_cols = ['date', 'time_dimension_begin', 'time_dimension_end']
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        print(f"{col}: convertido para datetime")
    
    # Converte ano para int
    df['time_dimension_value'] = pd.to_numeric(df['time_dimension_value'], errors='coerce')
    print("time_dimension_value: convertido para int")
    
    return df
