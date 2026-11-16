from calculator import tempoCalculator
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Tempo Running Calculator",
    page_icon="🏃‍♂️‍➡️",
)

distance = st.number_input(label="Sprint distance", min_value=40, step=1, value=110, help="How far you sprinted")
time = st.number_input(label="Sprint time", min_value=3.00, step=0.01, value=10.2, help="Your PR for that distance")

sheet = tempoCalculator(distance, time)
percentages = []
for i in range(65, 100):
    percentages.append(f"**{i}%**")

chart = pd.DataFrame({"**Percentage**": percentages, "**Time**": sheet})
chart = chart.set_index("**Percentage**")

left = chart.iloc[:18]
right = chart.iloc[18:]

st.title("Tempo running chart:", help="The chart that shows how fast you need to run the distance at a given percentage of your PR speed")
col1, col2 = st.columns(2)
with col1:
    st.table(left.style.format({f"**Time**": "{:.2f} s"}))
with col2:
    st.table(right.style.format({f"**Time**": "{:.2f} s"}))
