# Imagem base recomendada e fixada para garantir reprodutibilidade
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia primeiro o arquivo de dependências para otimizar o cache de build
COPY requirements.txt .

# Instala as dependências sem armazenar cache do pip para reduzir o tamanho da imagem
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Documenta a porta que a aplicação utiliza
EXPOSE 5000

# Comando de inicialização do container
CMD ["python", "app.py"]