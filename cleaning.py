def clean_column_names(df):
    """
    Standardizes column names: lowercase, underscores instead of spaces.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace(r'[^a-z0-9_]', '', regex=True)
    )
    return df
