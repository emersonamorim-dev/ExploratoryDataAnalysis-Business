library(ggplot2)

# Você deve ter ggplot2 instalado para usar essas funções
# Função para plotar séries temporais de vendas
plot_time_series <- function(data, date_col, value_col) {
  ggplot(data, aes_string(x = date_col, y = value_col)) +
    geom_line(color = "blue") +
    labs(title = "Vendas ao Longo do Tempo",
         x = "Data",
         y = "Vendas") +
    theme_minimal()
}

# Função para plotar clusters de clientes em um scatter plot
plot_clusters <- function(data, x_col, y_col, cluster_col) {
  ggplot(data, aes_string(x = x_col, y = y_col, color = cluster_col)) +
    geom_point() +
    labs(title = "Clusters de Clientes",
         x = x_col,
         y = y_col) +
    scale_color_discrete(name = "Cluster") +
    theme_minimal()
}


