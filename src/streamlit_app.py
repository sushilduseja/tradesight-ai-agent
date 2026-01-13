"""
TradeSight Alert Triage Dashboard

Streamlit interface for surveillance analysts to:
1. View alert queue with priority sorting
2. Analyze individual alerts using multi-agent system
3. Review agent reasoning and recommendations
4. Log override decisions with audit trail

Production note: This prototype will be replaced with React frontend
for production deployment with enhanced UX and performance.
"""

import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide", page_title="TradeSight - Alert Triage")

st.title("TradeSight AI - Alert Triage Dashboard")
st.markdown("Multi-agent system for trade surveillance alert analysis")

# Mock alert queue data
alert_data = {
    "Alert ID": ["ALT_001", "ALT_002", "ALT_003"],
    "Priority": ["High", "Medium", "Low"],
    "Type": ["Spoofing", "Layering", "Front-running"],
    "Trader ID": ["T12345", "T67890", "T13579"],
}
alerts_df = pd.DataFrame(alert_data)

st.header("Alert Queue")
st.dataframe(alerts_df, use_container_width=True)

st.header("Analyze Alert")
selected_alert = st.selectbox("Select an alert to analyze:", alerts_df["Alert ID"])

if st.button("Analyze"):
    with st.spinner(f"Analyzing {selected_alert}..."):
        # Production: Call FastAPI backend
        # api_url = "http://api:8000/api/v1/alerts/analyze"
        # response = requests.post(
        #     api_url,
        #     json={"alert_id": selected_alert, "priority": "high", "context_depth": "full"}
        # )
        # mock_response = response.json()
        
        # Mock response for demonstration
        mock_response = {
            "alert_id": selected_alert,
            "recommendation": "ESCALATE",
            "confidence_level": "high",
            "reasoning": {
                "summary": "Trading pattern consistent with spoofing behavior",
                "evidence": {
                    "trade_anomaly": "Large orders placed and cancelled within 500ms",
                    "historical_similarity": "Matches 3 confirmed spoofing cases",
                    "communication_signals": "No suspicious communications detected"
                }
            },
            "suggested_actions": [
                "Review complete order log for trader T12345",
                "Interview trader regarding order placement strategy",
            ],
        }

        st.subheader(f"Analysis for {mock_response['alert_id']}")
        
        
        col1, col2 = st.columns(2)
        col1.metric("Recommendation", mock_response["recommendation"])
        col2.metric("Confidence", mock_response["confidence_level"])

        st.subheader("Reasoning")
        st.write(mock_response["reasoning"]["summary"])
        st.json(mock_response["reasoning"]["evidence"])

        st.subheader("Suggested Next Steps")
        for action in mock_response["suggested_actions"]:
            st.write(f"- {action}")
