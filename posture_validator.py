# posture_validator.py

import streamlit as st
import pandas as pd
import requests
import os
from io import StringIO

# CONFIGURE YOUR GEMINI API KEY HERE
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY") or "YOUR_API_KEY_HERE"

# Set Streamlit UI
st.set_page_config(page_title="Posture Validator", layout="wide")
st.title("🔐 PAN-OS Security Posture Validator")

uploaded_file = st.file_uploader("Upload your PAN-OS config (XML or JSON)", type=["xml", "json"])

# AI prompt template
prompt_template = """
You are a security expert specializing in Palo Alto Networks PAN-OS configurations.
Analyze the following PAN-OS configuration and identify potential security gaps, misconfigurations, or areas that do not meet best practices.
Generate a professional summary and tabular report.

Configuration:
{config_content}

Return format:
1. Summary (Markdown)
2. Table (CSV format): Section, Issue, Severity, Recommendation
"""

# Gemini API function (REST call)
def call_gemini_api(prompt):
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    res = requests.post(endpoint, headers=headers, json=body)

    if res.status_code == 200:
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        st.error(f"❌ Error: {res.status_code} - {res.text}")
        return None

# App logic
if uploaded_file:
    config_str = uploaded_file.read().decode("utf-8")
    st.info("Analyzing file with Gemini...")
    prompt = prompt_template.format(config_content=config_str)

    with st.spinner("Running Gemini analysis..."):
        result = call_gemini_api(prompt)

    if result:
        if "Section,Issue,Severity,Recommendation" in result:
            summary, csv_data = result.split("Section,Issue,Severity,Recommendation", 1)
            csv_data = "Section,Issue,Severity,Recommendation" + csv_data

            st.subheader("📝 Summary")
            st.markdown(summary.strip())

            st.subheader("📊 Issues Table")
            df = pd.read_csv(StringIO(csv_data))
            st.dataframe(df)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download CSV Report", csv, "posture_report.csv", "text/csv")
        else:
            st.warning("⚠️ AI output was returned but didn’t contain a proper CSV. Please review formatting.")
    else:
        st.warning("⚠️ Unable to generate output. Check your API key or file formatting.")
else:
    st.info("📂 Upload a PAN-OS config file to begin.")
