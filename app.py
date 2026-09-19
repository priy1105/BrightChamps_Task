import streamlit as st
import requests
import time

# --- CONFIGURATION ---
# 1. Your n8n Production Webhook URL
WEBHOOK_URL = "https://priyanshu-agents.app.n8n.cloud/webhook-test/deploy-latency-bridge"

# 2. Your Google Sheet ID (the long string in the URL)
SHEET_ID = "1W7tGtN3weAsBQ9fmT42Swjte1SNXlPT8xw_FP0fIx3g" 

# 3. The public link to your Google Sheet (Make sure it's set to 'Anyone with link can edit')
SHEET_LINK = "https://docs.google.com/spreadsheets/d/1W7tGtN3weAsBQ9fmT42Swjte1SNXlPT8xw_FP0fIx3g/edit?usp=sharing"
# ---------------------

st.set_page_config(page_title="BrightChamps Task - By Priyanshu", page_icon="🚀", layout="centered")

st.title("🚀 Founder's Office: BrightChamps")
st.markdown("Assignment - Priyanshu - B.Tech., NITK Surathkal")
st.divider()
st.subheader("Step 1: Stage the Google Sheets CRM")
st.markdown(f"Open the **[Live Google Sheets]({SHEET_LINK})** (linked to n8n) and add your 4-5 test leads to the bottom row. Set the `demo_scheduled_at` to a future time.")

st.write("") 

st.subheader("Step 2: Dispatch the Workflow")
st.markdown("Clicking below triggers the n8n webhook, scans the sheet, and executes the process.")

if st.button("⚡ Start the n8n Engine", type="primary", use_container_width=True):
    with st.status("Initiating API handshake...", expanded=True) as status:
        time.sleep(1) 
        
        try:
            payload = {"sheet_id": SHEET_ID}
            response = requests.post(WEBHOOK_URL, json=payload)
            
            if response.status_code == 200:
                status.update(label="Sequence Successfully Dispatched!", state="complete", expanded=False)
                st.success("n8n pipeline active. Check the Google Sheet to see your row lock turn to 'Active'.")
                st.balloons()
            else:
                status.update(label="Dispatch Failed", state="error", expanded=True)
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            status.update(label="Connection Error", state="error", expanded=True)
            st.error(f"Failed to connect to n8n: {str(e)}")
