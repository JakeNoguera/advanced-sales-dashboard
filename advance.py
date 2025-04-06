import streamlit as st
import pandas as pd
import plotly.express as px

#cd Advance
#streamlit run advance.py


# Load the dataset
df = pd.read_csv("sales_advanced.csv")

st.set_page_config(page_title="Advanced Sales Dashboard", layout="wide")
st.title("📊 Advanced Sales Dashboard (Q1 2023)")

# Sidebar filters
region_filter = st.sidebar.selectbox("Filter by Region:", df["Region"].unique())
segment_filter = st.sidebar.selectbox("Filter by Segment:", df["Segment"].unique())

filtered_df = df[(df["Region"] == region_filter) & (df["Segment"] == segment_filter)]

# 1️⃣ Interactive Line Chart: Sales Trend by Region
st.subheader("📈 Sales Trend by Region")
line_chart = px.line(filtered_df, x="Date", y="Sales", color="Product", markers=True)
st.plotly_chart(line_chart, use_container_width=True)

# 2️⃣ Animated Bar Chart: Monthly Product Sales
st.subheader("📊 Animated Product Sales by Month")
bar_chart = px.bar(df, x="Product", y="Sales", color="Region", animation_frame="Month", barmode="group")
st.plotly_chart(bar_chart, use_container_width=True)

# 3️⃣ Pie Chart: Sales by Customer Segment
st.subheader("🧩 Sales Distribution by Segment")
pie_data = df.groupby("Segment")["Sales"].sum().reset_index()
pie_chart = px.pie(pie_data, names="Segment", values="Sales", title="Sales by Segment", hole=0.4)
st.plotly_chart(pie_chart, use_container_width=True)

# 4️⃣ Filtered Table
st.subheader("📋 Filtered Sales Table")
st.dataframe(filtered_df.reset_index(drop=True))

# 5️⃣ Heatmap (Sales by Region and Product)
st.subheader("🔥 Sales Heatmap (Region vs Product)")
heatmap_data = df.pivot_table(index="Region", columns="Product", values="Sales", aggfunc="sum")
st.dataframe(heatmap_data.style.background_gradient(cmap='Blues'))

st.markdown("---")
st.markdown("✅ Built with Python, Pandas, Plotly, and Streamlit")