# Use a imagem oficial do Python
FROM python:3.9

# Define a variável de ambiente para evitar problemas com a saída padrão do Python
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho no contêiner
WORKDIR /code

# Instala as dependências do projeto
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o código fonte para o contêiner
COPY . .

# Comando para executar as migrações e iniciar o servidor
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "--insecure"]