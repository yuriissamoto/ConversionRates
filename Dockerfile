# Use a imagem base do Python
FROM python:3

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copie o código do backend para a pasta de trabalho
COPY .

# Exponha a porta em que o servidor Django estará rodando
EXPOSE 8000

# Comando para executar a aplicação Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]