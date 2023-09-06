import pandas as pd

def load_csv(df, file_path):
    """
    Carrega dados processados em um arquivo CSV.
    :param df: DataFrame com os dados processados
    :param file_path: Caminho onde o arquivo CSV será salvo
    """
    df.to_csv(file_path, index=False)


