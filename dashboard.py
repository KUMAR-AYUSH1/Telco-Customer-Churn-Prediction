import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
st.title("Dashbord")

st.sidebar.header("📌 About")

st.sidebar.info(
    """
    This model was trained on the **Telco Customer Churn Dataset**
    using **XGBoost + Optuna Hyperparameter Tuning**.

    ### 🚀 Best Model Parameters
    - learning_rate: 0.13
    - max_depth: 1
    - n_estimators: 200
    - min_child_weight: 9
    - subsample: 0.91
    - colsample_bytree: 0.72

    ### 📊 Model Performance
    - Accuracy Score: **0.777**
    - Precision Score: **0.741**
    - Recall Score: **0.853**
    - F1 Score: **0.793**
    - ROC AUC Score: **0.845**

    ### 🔍 Confusion Matrix
    ```
    [[254 108]
     [ 53 309]]
    ```
    """
)

st.markdown("""
This dashboard provides visual analysis of the **Telco Customer Churn Dataset**  
and model prediction performance.
""")
st.write("These plot shows the Dataset  for Telco Churn Prediction vs churn counts")
image_folder = Path("plots")
images = [img for img in image_folder.iterdir() if img.is_file()]
for image in images:
    st.image(image)


st.divider()
st.write("These plot shows correct prediction vs wrong prediction of  xgb model for Telco Churn Prediction on different features")
image_folder = Path("model_plot")
images = [img for img in image_folder.iterdir() if img.is_file()]
for image in images:
    st.image(image)