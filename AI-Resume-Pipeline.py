

# app.py

import streamlit as st

st.set_page_config(
    page_title="Explainable ATS Resume Screening",
    layout="wide"
)

st.title("🤖 Explainable ATS Resume Screening System")

st.markdown("""
This app acts as an **intermediary between HR teams and candidates**.

- 🧑‍💼 **HR Panel** – Understand model **fairness**, **bias**, and decision patterns.  
- 🙋‍♀️ **Candidate Panel** – See **why a resume was rejected** and **how to improve it**.  
- 📊 **Visual Analytics** – Compare **selected vs rejected** resumes.

Use the left sidebar pages:
- **Fairness Analysis**
- **Resume Evaluation**
- **Rejection Explanation & Improvement**
- **Visual Insights**
- **Advanced ATS Insights
- **Resume Comparison -( Strong Vs Weak )
""")

