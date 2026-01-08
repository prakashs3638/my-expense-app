import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. Setup Page Configuration
st.set_page_config(
    page_title="Expense Tracker 2026",
    layout="wide"
)

# 2. Page Title
st.title("Personal Expense Dashboard")

# 3. Setup Data Storage (Local CSV for simplicity)
DATA_FILE = "expenses.csv"  # Add quotes around the file name

try:
    df = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])  # Add quotes to column names

# 4. Sidebar for Data Entry
st.sidebar.header("Add New Expense")  # Quotes around the header text
with st.sidebar.form("expense_form", clear_on_submit=True):  # Form name should be in quotes
    d = st.date_input("Date", date.today())  # Add quotes around the labels
    cat = st.selectbox("Category", ["Travel", "Meals", "Office", "Software", "Other"])  # Added quotes around category options
    amt = st.number_input("Amount ($)", min_value=0.0, step=0.01)  # Added quotes around the label
    note = st.text_input("Note")  # Added quotes around the label
    submitted = st.form_submit_button("Add Expense")  # Added quotes for button label

    if submitted:
        # Add new expense to dataframe
        new_row = pd.DataFrame([[d, cat, amt, note]], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)  # Save to CSV
        st.success("Expense added!")  # Added quotes around the success message

# 5. Main Dashboard Visuals
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Recent Logs")  # Added quotes for subheader text
    st.dataframe(df.tail(10), use_container_width=True)

with col2:
    if not df.empty:
        st.subheader("Spending by Category")  # Added quotes for subheader text
        fig = px.pie(df, values="Amount", names="Category", hole=0.4)  # Added quotes for column names
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data yet. Add an expense in the sidebar!")  # Added quotes for the info message
