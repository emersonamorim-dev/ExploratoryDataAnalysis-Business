import os
import pandas as pd
from libs.data_cleaning import handle_missing_values, transform_data_types, remove_outliers

# Constantes definidas na parte superior do módulo
SALES_DATA_PATH = "/home/youruser/myproject/ExploratoryDataAnalysis-Business/data/processed/sales_data.csv"
USER_ACTIVITY_PATH = "/home/youruser/myproject/ExploratoryDataAnalysis-Business/data/processed/user_activity.csv"

def transform_sales_data(df):
    """
    Transforma dados brutos de vendas.
    :param df: DataFrame com dados brutos de vendas
    :return: DataFrame transformado
    """
    df = handle_missing_values(df)
    column_types = {
        "Date": "datetime64",
        "ProductID": "int32",
        "Amount": "float32"
    }
    df = transform_data_types(df, column_types)
    df = remove_outliers(df, "Amount")
    df['SaleYearMonth'] = df['Date'].dt.to_period('M')
    return df

def transform_user_activity(df):
    """
    Transforma dados brutos de atividades dos usuários.
    :param df: DataFrame com dados brutos de atividades dos usuários
    :return: DataFrame transformado
    """
    df = handle_missing_values(df)
    if 'timestamp' in df.columns:
        # ConvertE para datetime antes de extrair propriedades
        df['timestamp'] = pd.to_datetime(df['timestamp'])  
        df['day_of_week'] = df['timestamp'].dt.dayofweek
        df['hour_of_day'] = df['timestamp'].dt.hour
    return df

def run():
    if not os.path.exists(SALES_DATA_PATH) or not os.path.exists(USER_ACTIVITY_PATH):
        print("Erro: Arquivos CSV não encontrados!")
        return

    print("Carregando dados...")
    sales_df = pd.read_csv(SALES_DATA_PATH)
    user_activity_df = pd.read_csv(USER_ACTIVITY_PATH)

    print("Transformando dados de vendas...")
    sales_df_transformed = transform_sales_data(sales_df)
    print("Transformando dados de atividades dos usuários...")
    user_activity_df_transformed = transform_user_activity(user_activity_df)

    print("Salvando os dados transformados...")
    sales_df_transformed.to_csv("sales_data_transformed.csv", index=False)
    user_activity_df_transformed.to_csv("user_activity_transformed.csv", index=False)
    
    print("Transformação completa!")
    return sales_df_transformed, user_activity_df_transformed

if __name__ == "__main__":
    run()
