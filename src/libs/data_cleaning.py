import pandas as pd

def handle_missing_values(df, strategy="mean"):
    """
    Preenche valores ausentes com a estratégia especificada.
    Estratégias suportadas: "mean", "median", "mode", "drop"
    """
    if strategy == "mean":
        return df.fillna(df.mean())
    elif strategy == "median":
        return df.fillna(df.median())
    elif strategy == "mode":
        return df.fillna(df.mode().iloc[0])
    elif strategy == "drop":
        return df.dropna()
    else:
        raise ValueError("Estratégia não suportada")

def transform_data_types(df, column_types):
    """
    Transforma os tipos de colunas conforme especificado.
    :param df: DataFrame de entrada
    :param column_types: Dicionário com {nome_da_coluna: tipo_desejado}
    """
    for column, dtype in column_types.items():
        df[column] = df[column].astype(dtype)
    return df

def remove_outliers(df, column, method="IQR", threshold=1.5):
    """
    Remove outliers de uma coluna específica.
    Métodos suportados: "IQR", "Z-score"
    """
    if method == "IQR":
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        df = df[~((df[column] < (Q1 - threshold * IQR)) | (df[column] > (Q3 + threshold * IQR)))]
    elif method == "Z-score":
        from scipy.stats import zscore
        zs = zscore(df[column])
        df = df[(zs > -threshold) & (zs < threshold)]
    else:
        raise ValueError("Método não suportado")

    return df

