FROM python:3.11-slim
WORKDIR /app
COPY index.py .
RUN pip install kafka-python
CMD ["python", "-u", "index.py"]