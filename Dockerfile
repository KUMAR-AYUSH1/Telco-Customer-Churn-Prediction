FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY plots/ plots/
COPY model_plot/ model_plot/
COPY model.pkl model.pkl
COPY ct.pkl ct.pkl
COPY main.py main.py
COPY app.py app.py
COPY  dashboard.py dashboard.py
COPY api.py api.py

EXPOSE 8000
EXPOSE 8501
CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port 8000 & streamlit run main.py --server.port 8501 --server.address 0.0.0.0"]