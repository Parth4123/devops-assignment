FROM python:3.9-slim
WORKDIR /app
COPY log-generator.py .
CMD ["python", "log-generator.py"]
