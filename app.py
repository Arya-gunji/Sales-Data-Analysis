from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Sales Analysis", page_icon="📊", layout="wide")
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #101a3a 0%, #211d3d 55%, #29213e 100%); color: #f8fafc; }
[data-testid="stMetric"] { background: rgba(20, 50, 100, .78); border: 1px solid #7185b8; padding: 16px; border-radius: 10px; }
[data-testid="stMetricLabel"], [data-testid="stMetricValue"] { color: #ffffff; }
section[data-testid="stSidebar"] { background-color: #102a50; }
h1, h2, h3, p, label { color: #f8fafc; }
</style>
""", unsafe_allow_html=True)

st.title("SALES ANALYSIS")
st.caption("Retail performance overview | Filter the data using the sidebar")

DEFAULT_DATA = Path(__file__).parent / "filtered_sales_data.csv"

@st.cache_data
def load_data(uploaded_file=None):
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_csv(DEFAULT_DATA)
    data.columns = [str(c).strip() for c in data.columns]
    required = ["Order ID", "Order Date", "Customer ID", "Segment", "Region", "State",
                "Category", "Sales", "Quantity", "Discount", "Profit"]
    missing = [c for c in required if c not in data.columns]
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(missing))
    data = data.drop_duplicates().copy()
    data["Order Date"] = pd.to_datetime(data["Order Date"], errors="coerce")
    for c in ["Sales", "Profit", "Quantity", "Discount"]:
        data[c] = pd.to_numeric(data[c], errors="coerce")
    data = data.dropna(subset=["Order Date", "Sales", "Profit", "Quantity"])
    data = data[data["Sales"] >= 0].copy()
    data["Year"] = data["Order Date"].dt.year
    data["Month"] = data["Order Date"].dt.month
    data["Year-Month"] = data["Order Date"].dt.to_period("M").astype(str)
    return data

with st.sidebar:
    st.header("Filters")
    uploaded = st.file_uploader("Upload your own CSV", type=["csv"])
    try:
        raw = load_data(uploaded)
    except Exception as exc:
        st.error(str(exc))
        st.stop()
    years = sorted(raw["Year"].dropna().unique().tolist())
    selected_years = st.multiselect("Year", years, default=years)
    regions = sorted(raw["Region"].dropna().unique().tolist())
    selected_regions = st.multiselect("Region", regions, default=regions)
    segments = sorted(raw["Segment"].dropna().unique().tolist())
    selected_segments = st.multiselect("Segment", segments, default=segments)
    categories = sorted(raw["Category"].dropna().unique().tolist())
    selected_categories = st.multiselect("Category", categories, default=categories)

data = raw[
    raw["Year"].isin(selected_years)
    & raw["Region"].isin(selected_regions)
    & raw["Segment"].isin(selected_segments)
    & raw["Category"].isin(selected_categories)
].copy()

if data.empty:
    st.warning("No records match the selected filters. Please adjust the filters.")
    st.stop()

total_orders = data["Order ID"].nunique()
total_customers = data["Customer ID"].nunique()
total_profit = data["Profit"].sum()
total_sales = data["Sales"].sum()
discount_value = (data["Sales"] * data["Discount"]).sum()
quantity = data["Quantity"].sum()
margin = total_profit / total_sales * 100 if total_sales else 0

k1, k2, k3 = st.columns(3)
k1.metric("TOTAL ORDERS", f"{total_orders:,}")
k2.metric("TOTAL CUSTOMERS", f"{total_customers:,}")
k3.metric("TOTAL NET PROFIT", f"${total_profit:,.0f}")
k4, k5, k6 = st.columns(3)
k4.metric("TOTAL SALES INCOME", f"${total_sales:,.0f}")
k5.metric("EST. DISCOUNT VALUE", f"${discount_value:,.0f}")
k6.metric("TOTAL QUANTITY", f"{quantity:,.0f}")

left, right = st.columns([1.4, 1])
with left:
    st.subheader("Sales by Month")
    monthly = data.groupby("Year-Month", as_index=False).agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    fig = px.line(monthly, x="Year-Month", y="Sales", markers=True, template="plotly_dark",
                  hover_data={"Profit":":,.2f"}, title="Monthly sales trend")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Sales Target")
    fig = go.Figure(go.Indicator(mode="gauge+number", value=total_sales/1_000_000,
        number={"prefix":"$","suffix":"M","valueformat":".2f"},
        title={"text":"Sales (millions)"}, gauge={"axis":{"range":[0, max(1, total_sales/1_000_000*1.25)]},
        "bar":{"color":"#4ea5ff"}, "steps":[{"range":[0, max(1, total_sales/1_000_000*0.5)],"color":"#25385f"},
        {"range":[max(1, total_sales/1_000_000*0.5), max(1, total_sales/1_000_000*1.25)],"color":"#384a70"}]}))
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", height=300, margin=dict(t=50,b=10,l=20,r=20))
    st.plotly_chart(fig, use_container_width=True)
    st.metric("PROFIT MARGIN", f"{margin:.2f}%")

c1, c2 = st.columns(2)
with c1:
    st.subheader("Sales by Region")
    reg = data.groupby("Region", as_index=False)["Sales"].sum().sort_values("Sales", ascending=True)
    fig = px.bar(reg, x="Sales", y="Region", orientation="h", text_auto=".2s", template="plotly_dark")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)
with c2:
    st.subheader("Sales by State")
    states = data.groupby("State", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False).head(10)
    fig = px.bar(states.sort_values("Sales"), x="Sales", y="State", orientation="h", text_auto=".2s", template="plotly_dark")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

c3, c4 = st.columns(2)
with c3:
    st.subheader("Sales by Segment and Category")
    seg_cat = data.groupby(["Segment", "Category"], as_index=False)["Sales"].sum()
    fig = px.bar(seg_cat, x="Segment", y="Sales", color="Category", barmode="stack", template="plotly_dark")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)
with c4:
    st.subheader("Profit by Category")
    cat = data.groupby("Category", as_index=False).agg(Sales=("Sales","sum"), Profit=("Profit","sum"))
    fig = px.bar(cat, x="Category", y="Profit", color="Category", template="plotly_dark")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Discount vs Profit")
fig = px.scatter(data, x="Discount", y="Profit", color="Category", hover_data=["State","Segment","Sales"],
                 template="plotly_dark", opacity=.7)
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Key Insights")
best_month = monthly.loc[monthly["Sales"].idxmax()]
best_region = data.groupby("Region")["Sales"].sum().idxmax()
best_category = data.groupby("Category")["Sales"].sum().idxmax()
best_state = data.groupby("State")["Sales"].sum().idxmax()
st.markdown(f"""
- **Highest-sales month:** {best_month['Year-Month']} (${best_month['Sales']:,.2f})
- **Top region by sales:** {best_region}
- **Top category by sales:** {best_category}
- **Top state by sales:** {best_state}
- **Overall profit margin:** {margin:.2f}%
""")
st.caption("Dataset note: included records are synthetic sample data for demonstration, not actual company sales.")

st.subheader("Filtered data")
st.dataframe(data, use_container_width=True, hide_index=True)
st.download_button("Download filtered data as CSV", data.to_csv(index=False).encode("utf-8"),
                   file_name="filtered_sales_data.csv", mime="text/csv")
