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
st.write("Dates")
st.write(df)
df["Sales"] = np.random.randint(low = 100, high = 500, size = len(dates))
st.write(df)

df["Expenses"] = np.random.randint(low = 50, high = 300, size = len(dates))
st.write(df)

df["Profit"] = df["Sales"] - df["Expenses"]
st.write(df)
