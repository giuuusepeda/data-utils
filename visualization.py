import matplotlib.pyplot as plt

def plot_line(df, x, y, title="Line Plot"):
    """
    Plots a simple line graph.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df[x], df[y], marker='o')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.show()
