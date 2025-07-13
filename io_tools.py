def save_to_csv(df, filename):
    """
    Saves a DataFrame to a CSV file without index.
    """
    df.to_csv(filename, index=False)
