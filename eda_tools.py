import pandas as pd
def smart_summary(df):
    """
    Resumo inteligente estilo R summary(), adaptado ao tipo de variável.
    Funciona com qualquer DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame a resumir.
    
    Returns:
        dict: Resumo das colunas.
    """
    summary = {}
    
    for col in df.columns:
        col_data = df[col]
        col_summary = {}
        
        # Contagem de valores não nulos e nulos
        col_summary['non_null_count'] = col_data.notnull().sum()
        col_summary['null_count'] = col_data.isnull().sum()
        col_summary['dtype'] = col_data.dtype.name
        
        if pd.api.types.is_numeric_dtype(col_data):
            col_summary['mean'] = col_data.mean()
            col_summary['std'] = col_data.std()
            col_summary['min'] = col_data.min()
            col_summary['25%'] = col_data.quantile(0.25)
            col_summary['50% (median)'] = col_data.median()
            col_summary['75%'] = col_data.quantile(0.75)
            col_summary['max'] = col_data.max()
            
        elif pd.api.types.is_categorical_dtype(col_data) or pd.api.types.is_object_dtype(col_data):
            col_summary['unique'] = col_data.nunique()
            top_value = col_data.value_counts().head(1)
            if not top_value.empty:
                col_summary['top'] = top_value.index[0]
                col_summary['freq'] = top_value.iloc[0]
            
        elif pd.api.types.is_datetime64_any_dtype(col_data):
            col_summary['min_date'] = col_data.min()
            col_summary['max_date'] = col_data.max()
            col_summary['unique_dates'] = col_data.nunique()
        
        else:
            col_summary['note'] = "Tipo não suportado para resumo detalhado."
        
        summary[col] = col_summary
    
    return pd.DataFrame(summary).T
