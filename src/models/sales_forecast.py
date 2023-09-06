import pandas as pd
from fbprophet import Prophet

def train_sales_forecast_model(df, columns_mapping):
    """
    Treina um modelo de previsão de vendas usando Prophet.
    :param df: DataFrame contendo dados históricos de vendas.
    :param columns_mapping: Um dicionário mapeando colunas para "ds" (tempo) e "y" valor a ser previsto.
    :return: Modelo treinado.
    """

    # Verificar se o DataFrame contém as colunas necessárias
    for col in columns_mapping.values():
        if col not in df.columns:
            raise ValueError(f"Coluna '{col}' não encontrada no DataFrame.")
    
    # Renomeia as colunas do DataFrame para que correspondam às expectativas de Prophet.
    df = df.rename(columns=columns_mapping)

    # Cria um modelo Prophet.
    model = Prophet()

    # Treina o modelo nos dados históricos.
    model.fit(df)

    # Retorna o modelo treinado.
    return model

def predict_sales(model, future_days):
    """
    Prevê vendas para um número especificado de dias.

    :param model: Modelo treinado de previsão de vendas.
    :param future_days: Número de dias a serem previstos.
    :return: DataFrame contendo previsões.
    """

    # Certificar-se de que future_days é positivo
    if future_days <= 0:
        raise ValueError("O número de dias para previsão deve ser positivo.")

    # Cria um DataFrame de previsão com os próximos `future_days` períodos de tempo.
    future = model.make_future_dataframe(periods=future_days)

    # Realiza a previsão usando o modelo treinado.
    forecast = model.predict(future)

    # Retorna o DataFrame de previsão.
    return forecast


