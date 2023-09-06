library(ggplot2)
library(dplyr)

# Carregar os dados (ajuste o caminho conforme necessário)
sales_data <- read.csv("../data/processed/sales_summary.csv")

# Análise de vendas ao longo do tempo
sales_over_time <- sales_data %>%
  group_by(Date) %>%
  summarise(Total_Sales = sum(Sales))

# Gráfico de vendas ao longo do tempo
ggplot(sales_over_time, aes(x = Date, y = Total_Sales)) +
  geom_line() +
  labs(title = "Vendas ao Longo do Tempo",
       x = "Data",
       y = "Vendas") +
  theme_minimal()

# Top 10 produtos mais vendidos
top_products <- sales_data %>%
  group_by(Product) %>%
  summarise(Total_Sold = sum(Quantity)) %>%
  arrange(-Total_Sold) %>%
  head(10)

# Gráfico dos produtos mais vendidos
ggplot(top_products, aes(x = reorder(Product, Total_Sold), y = Total_Sold)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  labs(title = "Top 10 Produtos Mais Vendidos",
       x = "Produto",
       y = "Quantidade Vendida") +
  theme_minimal()

