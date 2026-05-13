# Telco Customer Churn Prediction 📉

An end-to-end **Customer Churn Prediction System** built using **Machine Learning, Optuna, FastAPI, Streamlit, Docker, and CI/CD concepts**.

The project predicts whether a telecom customer is likely to churn and provides:

* Churn prediction
* Churn probability
* Suggested discount strategy

---

## 🚀 Tech Stack

* Python
* Scikit-learn
* XGBoost
* Optuna
* FastAPI
* Streamlit
* Docker
* GitHub Actions

---

## 📦 Docker Image

Pull the Docker image directly from Docker Hub:

```bash
docker pull kumar2700/telco-churn-prediction:latest
```

---

## 📊 Dataset

Dataset used from Kaggle:

```text
https://www.kaggle.com/datasets/blastchar/telco-customer-churn
```

---

# 📁 Project Structure

## 🔹 preprocess.ipynb

Data preprocessing pipeline including:

* Data cleaning
* Feature selection
* Handling class imbalance
* Encoding & transformations

Also saves:

* `preprocess.csv` → processed dataset for model training
* `sample.csv` → sample dataset for testing data drift & model drift

---

## 🔹 plots.ipynb

Performs Exploratory Data Analysis (EDA):

* Feature vs Churn analysis
* Visualization of different customer patterns

Saves generated plots inside:

```text
plots/
```

---

## 🔹 test1.ipynb

Model experimentation notebook.

Models tested:

* XGBoost
* SVC
* KNN
* Random Forest
* Logistic Regression

Uses **Optuna** for hyperparameter tuning.

### ✅ Best Model:

* XGBoost

---

## 🔹 test2.ipynb

Final XGBoost + Optuna evaluation.

### 📈 Model Performance

| Metric        | Score |
| ------------- | ----- |
| Accuracy      | 0.77  |
| Precision     | 0.741 |
| Recall        | 0.85  |
| F1 Score      | 0.79  |
| ROC-AUC Score | 0.845 |

### 🎯 Threshold Analysis

| Threshold | Best For                 |
| --------- | ------------------------ |
| 0.45      | Highest Recall           |
| 0.50      | Best Accuracy & F1 Score |
| 0.60      | Highest Precision        |

Additional features:

* Prediction analysis on different customer features
* Saves prediction plots in:

```text
model_plot/
```

Saved artifacts:

* `model.pkl`
* `ct.pkl`

---

## 🔹 try.ipynb

Notebook for:

* Data Drift Detection
* Model Drift Monitoring
* CI/CD experimentation

---

# 🌐 Application Files

## 🔹 api.py

FastAPI backend for:

* Churn prediction
* Churn probability estimation
* Discount type recommendation

---

## 🔹 app.py

Streamlit frontend connected with FastAPI.

Features:

* Real-time churn prediction
* Probability visualization
* Discount recommendation

---

## 🔹 dashboard.py

Streamlit dashboard displaying:

* EDA plots
* Model prediction plots

---

## 🔹 main.py

Main Streamlit multipage application combining:

* `app.py`
* `dashboard.py`

---

# 🐳 Docker Support

## 🔹 Dockerfile

Dockerized deployment for:

* FastAPI backend
* Streamlit frontend

---

# 📋 Requirements Files

## 🔹 requirements.txt

Dependencies required for:

* Main application
* Docker deployment

## 🔹 test_requirements.txt

Dependencies required for:

* Drift detection
* Monitoring notebooks
* Experimental testing

---

---

# 📌 Features

✅ End-to-end ML pipeline
✅ Hyperparameter tuning with Optuna
✅ Drift monitoring concepts
✅ FastAPI backend
✅ Streamlit frontend
✅ Dockerized deployment
✅ Threshold optimization analysis
✅ Interactive dashboards

---

<img width="662" height="301" alt="Screenshot 2026-05-14 021929" src="https://github.com/user-attachments/assets/22ed8897-16c1-4e58-a9e4-d9b949da2641" />


---


