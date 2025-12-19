import streamlit as st
import pandas as pd

st.title("🎾 Tennis Matrix Explorer")

# Load Excel file
file = "TennisMatrix.xlsx"
df = pd.read_excel(file, sheet_name=None)

# Sidebar navigation
sheet = st.sidebar.selectbox("Choose a section", list(df.keys()))

# Display selected sheet
st.subheader(sheet)
st.dataframe(df[sheet])
