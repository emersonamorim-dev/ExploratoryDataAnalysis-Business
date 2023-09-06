import pandas as pd

def extract_csv(file_path):
    """
    Extrai dados de um arquivo CSV.
    :param file_path: Caminho para o arquivo CSV
    :return: DataFrame com os dados extraídos
    """
    return pd.read_csv(file_path)

def run(file_path):
    """
    Função de execução para extração de dados.
    :param file_path: Caminho para a fonte de dados.
    :return: DataFrame com os dados extraídos.
    """
    return extract_csv(file_path)

# No futuro, a função run pode ser expandida para tratar diferentes tipos de fontes de dados, dependendo da lógica que você precisa.

