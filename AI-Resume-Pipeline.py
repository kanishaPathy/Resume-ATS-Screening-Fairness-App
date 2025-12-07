

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
st.write("")

# --- Buttons Navigation UI ---
col1, col2 = st.columns(2)

with col1:
    if st.button("📊 Fairness Analysis"):
        st.switch_page("pages/1_Fairness_Analysis.py")

    if st.button("📈 Visual Insights"):
        st.switch_page("pages/4_Dashboard_Insights.py")

with col2:
    if st.button("📝 Resume Evaluation"):
        st.switch_page("pages/2_Resume_Evaluation.py")

    if st.button("🔍 Advanced ATS Insights"):
        st.switch_page("pages/5_Advanced_ATS_Insights.py")

if st.button("⚠ Rejection Explanation & Improvement"):
    st.switch_page("pages/3_Rejection_Explanation.py")

if st.button("🆚 Resume Comparison (Strong vs Weak)"):
    st.switch_page("pages/6_Resume_Compare.py")


