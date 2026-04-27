import wbgapi as wb
import pandas as pd
import streamlit as st

@st.cache_data
def get_country_list():
    """Fetches the list of countries from the World Bank API."""
    return {p['value']: p['id'] for p in wb.economy.list() if len(p['id']) == 3}


def fetch_economic_data(indicator_id, country_id, indicator_name):
    """Downloads, transposes, and cleans data for a specific indicator and country."""
    # Download most recent 20 values
    df = wb.data.DataFrame(indicator_id, country_id, mrv=20).transpose()

    # Clean Year format (YR2022 -> 2022)
    df.index = df.index.str.replace('YR', '').astype(int)

    # Rename column and index
    df.columns = [indicator_name]
    df.index.name = "Year"
    df = df.reset_index()

    # Ensure numeric values
    df[indicator_name] = pd.to_numeric(df[indicator_name], errors='coerce')

    return df
