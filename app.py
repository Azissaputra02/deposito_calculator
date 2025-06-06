import streamlit as st
import pandas as pd
import altair as alt

# --- Page Configuration ---
st.set_page_config(page_title="Time Deposit Simulation", layout="wide")

# --- Header ---
st.markdown("""
<h1 style="
    font-size: 3em;
    font-weight: 900;
    background: linear-gradient(to right, #00b894, #0984e3, #ffffff);
    -webkit-background-clip: text;
    color: transparent;
    text-align: left;
    margin-top: -20px;
">
Time Deposit Simulation
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="color:white; font-size:1.1em;">
Simulate how your money grows in a year through time deposit options. Select two banks and tenors, and compare the performance of their products after 12 months.
</p>
""", unsafe_allow_html=True)

# --- Load Interest Rate Database ---
data = {
    'Bank': [...],  # Use your full bank/tenor/interest table here
    'Tenor': [...],
    'Interest': [...]
}
df_rate = pd.DataFrame(data)