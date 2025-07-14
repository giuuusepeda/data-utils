def clean_column_names(df):
    """
    Padroniza os nomes das colunas para minúsculas e underscores.
    
    Args:
        df (pd.DataFrame): DataFrame para limpar as colunas.
        
    Returns:
        pd.DataFrame: DataFrame com colunas limpas.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace(r'[^a-z0-9_]', '', regex=True)
    )
    return df


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




