FROM python:3.11-slim
WORKDIR /app
COPY index.py .
RUN pip install fastapi uvicorn kafka-python pydantic
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "80"]
