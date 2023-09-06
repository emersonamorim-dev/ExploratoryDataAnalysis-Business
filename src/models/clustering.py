from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def segment_customers(df, n_clusters):
    """
    Segmenta clientes em grupos usando KMeans.
    :param df: DataFrame contendo dados dos clientes.
    :param n_clusters: Número de clusters.
    :return: DataFrame com segmentos atribuídos.
    """
    
    # Verificar se há NaNs no DataFrame
    if df.isnull().sum().sum() > 0:
        raise ValueError("O DataFrame contém valores nulos. Por favor, trate-os antes de prosseguir.")
    
    # Certificar-se de que n_clusters é um valor válido
    if n_clusters <= 0 or n_clusters > df.shape[0]:
        raise ValueError("O número de clusters deve ser positivo e não maior do que o número de samples.")

    # É uma boa prática padronizar os dados antes do clustering
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(df)
    
    # KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    df['Cluster'] = kmeans.fit_predict(data_scaled)
    
    return df

