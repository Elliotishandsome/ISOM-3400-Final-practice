import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(
    start="2024-01-01",
    end="2024-06-30",
    freq="ME"
)
st.write(dates)

df = pd.DataFrame(dates, columns = ["Month"])
st.write(df)

df["Sales"] = np.random.randint(low = 100, high = 500, size = len(dates))
st.write(df)

df["Expenses"] = np.random.randint(low = 50, high = 300, size = len(dates))
st.write(df)

df["Profit"] = df["Sales"] - df["Expenses"]
st.write(df)

show_expense = st.checkbox("Show Expenses")

sales_thresold = st.slider("Minimum Sales", 100, 500, 300)
filtered_data = df[df["Sales"] >= sales_thresold]
st.write(filtered_data)

if show_expense:
    comparision_data = filtered_data.set_index("Month")[["Sales", "Expenses"]]
    st.line_chart(comparision_data)
else:
    sales_data = filtered_data.set_index("Month")["Sales"]
    st.line_chart(sales_data)

Total_sales = filtered_data["Sales"].sum()
st.write(f"Total_sales: {Total_sales}")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

selected_months = st.sidebar.multiselect(
    "Select Months",
    months,
    default=months
)

filtered_months = df[df["Month"].isin(selected_months)]
st.write(filtered_months)
