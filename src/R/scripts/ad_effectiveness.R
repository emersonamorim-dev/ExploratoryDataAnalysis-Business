library(ggplot2)
library(dplyr)

# Carregar os dados (ajuste o caminho conforme necessário)
sales_data <- read.csv("../data/processed/sales_summary.csv")

# Suponhamos que a campanha publicitária ocorreu em uma data específica
ad_campaign_date <- as.Date("2022-06-01")

# Segmentar dados antes e depois da campanha
pre_ad_data <- sales_data %>%
  filter(Date < ad_campaign_date)

post_ad_data <- sales_data %>%
  filter(Date >= ad_campaign_date)

# Comparar médias de vendas
mean_pre_ad <- mean(pre_ad_data$Sales)
mean_post_ad <- mean(post_ad_data$Sales)

print(paste("Média de vendas antes da campanha: ", mean_pre_ad))
print(paste("Média de vendas depois da campanha: ", mean_post_ad))

# Visualização
sales_comparison <- data.frame(
  Period = c("Antes da Campanha", "Depois da Campanha"),
  Sales = c(mean_pre_ad, mean_post_ad)
)

ggplot(sales_comparison, aes(x = Period, y = Sales)) +
  geom_bar(stat = "identity") +
  labs(title = "Comparação de Vendas Antes e Depois da Campanha",
       x = "Período",
       y = "Vendas Médias") +
  theme_minimal()

