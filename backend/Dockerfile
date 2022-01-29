FROM python:3.9

WORKDIR /app/backend

COPY requirements.txt ./
COPY entrypoint.sh ./

RUN pip install -r requirements.txt
RUN chmod +x ./entrypoint.sh

COPY . .
ENTRYPOINT ["sh", "/app/backend/entrypoint.sh"]
