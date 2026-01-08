import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

st.set_page_config(
    page_title="Expense Tracker 2026",
    layout="wide"
)
st.title("Personal Expense Dashboard")

# 1. Setup Data Storage (Local CSV for simplicity)
DATA_FILE = expenses.csv

try
    df = pd.read_csv(DATA_FILE)
except FileNotFoundError
    df = pd.DataFrame(columns=[Date, Category, Amount, Note])

# 2. Sidebar for Data Entry
st.sidebar.header(Add New Expense)
with st.sidebar.form(expense_form, clear_on_submit=True)
    d = st.date_input(Date, date.today())
    cat = st.selectbox(Category, [Travel, Meals, Office, Software, Other])
    amt = st.number_input(Amount ($), min_value=0.0, step=0.01)
    note = st.text_input(Note)
    submitted = st.form_submit_button(Add Expense)

    if submitted
        new_row = pd.DataFrame([[d, cat, amt, note]], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success(Expense added!)

# 3. Main Dashboard Visuals
col1, col2 = st.columns([1, 1])

with col1
    st.subheader(Recent Logs)
    st.dataframe(df.tail(10), use_container_width=True)

with col2
    if not df.empty
        st.subheader(Spending by Category)
        fig = px.pie(df, values='Amount', names='Category', hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
    else

        st.info(No data yet. Add an expense in the sidebar!)


