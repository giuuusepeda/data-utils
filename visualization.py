import matplotlib.pyplot as plt

def plot_line(df, x, y, title="Line Plot"):
    """
    Cria um gráfico de linha simples.
    
    Args:
        df (pd.DataFrame): DataFrame com dados a serem plotados.
        x (str): Nome da coluna para o eixo X.
        y (str): Nome da coluna para o eixo Y.
        title (str, opcional): Título do gráfico.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df[x], df[y], marker='o')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.show()
