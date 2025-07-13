def save_to_csv(df, filename):
    """
    Salva um DataFrame como arquivo CSV sem índice.
    
    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        filename (str): Nome do arquivo CSV.
    """
    df.to_csv(filename, index=False)
