# Lignes d'import / Import Lines
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page / Page config
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon= "📊",
    layout="wide"
)

# Charger les données / Load data
@st.cache_data
def load_data():
    df = pd.read_csv("./data/Sample - Superstore.csv", encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

df = load_data()

# Titre / Title
st.title("📊 Sales Dashboard")
st.markdown("Sales Analysis - General View")

# Filtres de la barre latérale / Sidebar filters
st.sidebar.header("🔍 Filters")

# Filtrer par année / Filter by year
years = sorted(df["Order Date"].dt.year.unique())
selected_years = st.sidebar.multiselect("Year", years, default=years)

# Filtrer par région / Filter by region
regions = sorted(df["Region"].unique())
selected_regions = st.sidebar.multiselect("Region", regions, default=regions)

# Filtrer par catégorie / Filter by category
categories = sorted(df["Category"].unique())
selected_categories = st.sidebar.multiselect("Category", categories, default=categories)

# Appliquer les fitres / Apply filters
df_filtered = df[
    (df["Order Date"].dt.year.isin(selected_years)) &
    (df["Region"].isin(selected_regions)) &
    (df["Category"].isin(selected_categories))
]

# KPIs
total_revenue = df_filtered["Sales"].sum()
total_orders = df_filtered["Order ID"].nunique()
avr_order_value = total_revenue / total_orders
total_profit = df_filtered["Profit"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Revenue", f"${total_revenue:.2f}")
col2.metric("🛒 Total Orders", f"{total_orders:,}")
col3.metric("🧾 Avg Order Value", f"${avr_order_value:.2f}")
col4.metric("📈 Total Profit", f"${total_profit:,.2f}")

# Séparateur visuel / Visual separator
st.markdown("---")

# Ligne 1 : 2 graphiques côte à côte / Line 1 : 2 graphs side by side
col1, col2 = st.columns(2)

# Vente par catégorie / Sales by catégorie
with col1:
    st.subheader("Sales by Category")
    fig_cat = px.bar(
        df_filtered.groupby("Category")["Sales"].sum().reset_index(),
        x="Category", y="Sales", color="Category"
    )
    st.plotly_chart(fig_cat, width="stretch")

# Ventes par régions / Sales by regions
with col2:
    st.subheader("Sales by Region")
    fig_region = px.pie(
        df_filtered.groupby("Region")["Sales"].sum().reset_index(),
        names="Region", values="Sales"
    )
    st.plotly_chart(fig_region, width="stretch")

# Ligne 2 : Évolution Temporelle / Line 2 : Evolution over time
st.markdown("---")
st.subheader("Revenue Over Time")
df_time = df_filtered.groupby("Order Date")["Sales"].sum().reset_index()
fig_time = px.line(df_time, x="Order Date", y="Sales")
st.plotly_chart(fig_time, width="stretch")

# Tableau détaillé / Detailed data
st.markdown("---")
st.subheader("📋 Detailed Data")

st.dataframe(
    df_filtered[
        ["Order Date",
        "Region",
        "Category",
        "Sub-Category",
        "Product Name",
        "Sales",
        "Quantity",
        "Profit"]
    ].sort_values("Order Date", ascending=False), width="stretch"
)


# # Prévisualisatiob / Preview
# st.dataframe(df_filtered.head(10))

# Pour lancer la commande run dans le terminal, utilisez la fonction suivante :
#  'streamlit run app.py'