import streamlit as st
import pandas as pd

# --- Configure page layout ---
st.set_page_config(page_title="Tennis Matrix Explorer", layout="wide")

st.title("🎾 Tennis Matrix Explorer")

# --- Load Excel file ---
file = "TennisMatrix.xlsx"
df = pd.read_excel(file, sheet_name="Technical Skills")

# --- Display table with editing enabled ---
st.subheader("Technical Skills")
edited_df = st.data_editor(df, num_rows="dynamic")

# --- Save changes back to Excel ---
if st.button("Save Changes"):
    edited_df.to_excel(file, sheet_name="Technical Skills", index=False)
    st.success("✅ Changes saved to Excel!")
