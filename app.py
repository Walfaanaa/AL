import pandas as pd

EXCEL_URL = "YOUR_RAW_GITHUB_URL"
EXCEL_URL = "https://raw.githubusercontent.com/Walfaanaa/atg/main/ATG.xlsx"
df = pd.read_excel(EXCEL_URL, engine="openpyxl")

st.title("EGSA Monthly Payment System")

st.dataframe(df)
