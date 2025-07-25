def save_to_csv(df, filename):
    """
    Salva um DataFrame como arquivo CSV pronto para Tableau Public PT-BR:
    - Sem índice
    - Separador ponto e vírgula (;)
    - Codificação utf-8-sig (compatível com acentos)

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        filename (str): Nome do arquivo CSV.
    """
    df.to_csv(filename, index=False, sep=";", encoding="utf-8-sig")
