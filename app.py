import streamlit as st
from utils.data_loader import load_data
from utils.analytics import volume_by_category, yes_price_distribution, top_markets

st.set_page_config(
    page_title="Prediction Market Intelligence",
    layout="wide"
)

st.title("📊 Prediction Market Intelligence")
st.write("A dashboard for analyzing prediction market trends and activity.")

# Load data
df = load_data()

# Sidebar filter
st.sidebar.header("Filters")
categories = df["category"].unique().tolist()
selected_categories = st.sidebar.multiselect(
    "Select Categories",
    categories,
    default=categories
)

filtered_df = df[df["category"].isin(selected_categories)]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Markets", len(filtered_df))
col2.metric("Total Volume", int(filtered_df["volume"].sum()))
col3.metric("Average YES Price", round(filtered_df["yes_price"].mean(), 2))

st.divider()

# Charts
st.subheader("Market Analytics")
st.plotly_chart(volume_by_category(filtered_df), use_container_width=True)
st.plotly_chart(yes_price_distribution(filtered_df), use_container_width=True)

st.divider()

# Top Markets Table
st.subheader("Top Markets by Volume")
st.dataframe(top_markets(filtered_df), use_container_width=True)
