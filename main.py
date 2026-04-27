import streamlit as st
import plotly.express as px
from utils.catalog import indicator_catalog
from utils.data_loader import get_country_list, fetch_economic_data

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Global Trade Explorer", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS ---
try:
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

try:
    # 2. LOAD INITIAL DATA
    countries_dict = get_country_list()
    country_names = sorted(countries_dict.keys())

    # --- SIDEBAR ---
    with st.sidebar:
        st.title("Settings")
        selected_country_name = st.selectbox("Select Country", country_names,
                                             index=country_names.index("Argentina") if "Argentina" in country_names else 0)
        country_id = countries_dict[selected_country_name]

        st.markdown("---")
        selected_category = st.selectbox("Indicator Category", list(indicator_catalog.keys()))
        available_indicators = list(indicator_catalog[selected_category].keys())
        selected_indicator_name = st.selectbox("Select Indicator", available_indicators)
        indicator_id = indicator_catalog[selected_category][selected_indicator_name]

    # --- MAIN CONTENT ---
    st.header(f"📈 {selected_country_name}")
    st.subheader(selected_indicator_name)

    # 3. FETCH DATA USING OUR UTILS
    df = fetch_economic_data(indicator_id, country_id, selected_indicator_name)

    if not df[selected_indicator_name].dropna().empty:
        # TOP METRICS
        m1, m2, m3 = st.columns(3)
        latest_val = df[selected_indicator_name].dropna().iloc[-1]
        max_val = df[selected_indicator_name].max()
        avg_val = df[selected_indicator_name].mean()

        with m1:
            st.metric("Latest Value", f"{latest_val:,.2f}")
        with m2:
            st.metric("All-time High", f"{max_val:,.2f}")
        with m3:
            st.metric("Period Average", f"{avg_val:,.2f}")

        st.markdown("---")

        # CHARTS AND TABLE
        col_left, col_right = st.columns([2, 1])

        with col_left:
            fig = px.area(df, x="Year", y=selected_indicator_name,
                          title=f"Time Series: {selected_indicator_name}",
                          markers=True)
            fig.update_layout(margin=dict(l=0, r=0, t=40, b=0), height=450)
            st.plotly_chart(fig, use_container_width=True)

        with col_right:
            st.write("#### Data Details")
            st.dataframe(df.sort_values("Year", ascending=False),
                         hide_index=True, use_container_width=True, height=400)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Export CSV", data=csv,
                               file_name=f"{country_id}_{selected_indicator_name}.csv",
                               mime='text/csv', use_container_width=True)
    else:
        st.warning("Insufficient data for the selected period.")

except Exception as e:
    st.error(f"Application error: {e}")

st.caption("Source: World Bank Open Data API")
