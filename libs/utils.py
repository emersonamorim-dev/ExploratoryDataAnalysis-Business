import pandas as pd
import os

def load_csv(file_path):
    """
    Carrega um arquivo CSV em um DataFrame.
    """
    if not os.path.exists(file_path):
        raise ValueError(f"O arquivo {file_path} não foi encontrado.")
    return pd.read_csv(file_path)

def save_csv(df, file_path, index=False):
    """
    Salva um DataFrame como arquivo CSV.
    """
    df.to_csv(file_path, index=index)

def get_unique_values(df, column):
    """
    Retorna valores únicos de uma coluna do DataFrame.
    """
    return df[column].unique()
