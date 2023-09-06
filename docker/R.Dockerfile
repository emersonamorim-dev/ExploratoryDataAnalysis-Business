FROM rocker/rstudio:4.1.0

# Mantenedor
LABEL maintainer="seuemail@exemplo.com"

# Instalando bibliotecas do sistema necessárias (ajuste conforme a necessidade)
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libxml2-dev \
    libssl-dev

# Instalando bibliotecas R (ajuste conforme a necessidade)
RUN R -e "install.packages(c('ggplot2', 'dplyr', 'tidyr', 'shiny'), dependencies=TRUE)"

# Expondo a porta padrão do RStudio
EXPOSE 8787

# Definindo a senha padrão para o RStudio (user: rstudio, password: password)
ENV PASSWORD password
