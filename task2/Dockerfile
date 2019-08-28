FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
CMD ["python","Teste.py"]
