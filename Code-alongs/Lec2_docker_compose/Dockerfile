FROM python:3.11

# host container
WORKDIR /app

COPY . .

RUN pip install plotly_express dash

EXPOSE 8050

CMD ["python", "./src/main.py"]