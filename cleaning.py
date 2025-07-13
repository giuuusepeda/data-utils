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
