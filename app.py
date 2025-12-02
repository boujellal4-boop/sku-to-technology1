
import streamlit as st
import pandas as pd
from io import BytesIO

# Predefined technology categories
TECH_CATEGORIES = [
    "Addressable",
    "Conventional",
    "Wireless",
    "Aspirating Smoke Detection",
    "Heat Detection",
    "Flame Detection",
    "Security-related Solutions"
]

st.title("SKU Technology Mapper")
st.write("Upload an Excel file with SKUs, and we'll replace SKUs with their technology category.")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    st.write("Preview of uploaded data:")
    st.dataframe(df.head())

    # Placeholder mapping logic using product_category
    def map_to_technology(row):
        category = str(row.get("product_category", "")).lower()
        if "fire" in category:
            if "aspirating" in category:
                return "Aspirating Smoke Detection"
            elif "heat" in category:
                return "Heat Detection"
            elif "flame" in category:
                return "Flame Detection"
            else:
                return "Addressable"
        elif "intrusion" in category or "security" in category:
            return "Security-related Solutions"
        elif "wireless" in category:
            return "Wireless"
        else:
            return "Conventional"

    # Apply mapping
    df["sku"] = df.apply(map_to_technology, axis=1)

    # Convert back to Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    st.download_button(
        label="Download Updated Excel",
        data=output.getvalue(),
        file_name="updated_orders.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
