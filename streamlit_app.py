import streamlit as st
from orchestrator import run_pipeline

st.title("AI Job Application Assistant")

jd = st.text_area("Paste Job Description")
resume = st.text_area("Paste Your Resume")

if st.button("Generate"):
    result = run_pipeline(jd, resume)

    if result:
        st.subheader("🔍 Job Analysis")
        st.text(result["jd_analysis"])

        st.subheader("📄 Improved Resume")
        st.text(result["resume"])

        st.subheader("✉️ Cover Letter")
        st.text(result["cover_letter"])