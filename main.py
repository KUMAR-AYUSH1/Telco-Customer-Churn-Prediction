import streamlit as st

dashboard_page = st.Page("dashboard.py", title="Analytics Dashboard", icon="📊")
prediction_page = st.Page("app.py", title="Run Predictions", icon="🤖")
pg = st.navigation([dashboard_page, prediction_page])
st.set_page_config(page_title="Data App", layout="wide")

pg.run()