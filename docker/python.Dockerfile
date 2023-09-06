FROM python:3.9-slim

# Mantenedor
LABEL maintainer="seuemail@exemplo.com"

# Definindo diretório de trabalho
WORKDIR /app

# Copiando requirements.txt assumindo que você tem este arquivo com todas as bibliotecas necessárias
COPY requirements.txt .

# Instalando as bibliotecas necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante dos arquivos opcional, pode ser adaptado conforme a necessidade
COPY . .

# Comando padrão ao iniciar o container
CMD ["python3"]
