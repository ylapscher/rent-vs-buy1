import streamlit as st
import pandas as pd
from utils.calculations import (
    calculate_total_buying_cost,
    calculate_total_renting_cost,
    calculate_mortgage_payment,
    calculate_breakeven_point
)
from utils.visualizations import (
    create_cost_comparison_chart,
    create_monthly_breakdown_chart,
    create_equity_chart
)

st.set_page_config(
    page_title="Rent vs. Buy Calculator",
    page_icon="🏠",
    layout="wide"
)

# Load custom CSS
with open('styles/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1>Rent vs. Buy Calculator</h1>
    <p>Make an informed decision about your next home</p>
</div>
""", unsafe_allow_html=True)

# Main calculator section
st.markdown('<div class="calculator-section">', unsafe_allow_html=True)

# Basic Inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("Purchase Options")
    purchase_price = st.number_input("Purchase Price ($)", min_value=0, value=300000, step=1000)
    down_payment = st.number_input("Down Payment ($)", min_value=0, value=60000, step=1000)
    annual_rate = st.number_input("Mortgage Rate (%)", min_value=0.0, value=3.5, step=0.1)
    years = st.number_input("Mortgage Term (years)", min_value=1, value=30, step=1)

with col2:
    st.subheader("Rental Options")
    monthly_rent = st.number_input("Monthly Rent ($)", min_value=0, value=2000, step=100)
    rent_increase_rate = st.number_input("Annual Rent Increase (%)", min_value=0.0, value=3.0, step=0.1)

# Advanced Options
with st.expander("Advanced Options"):
    col3, col4 = st.columns(2)
    
    with col3:
        property_tax_rate = st.number_input("Annual Property Tax Rate (%)", min_value=0.0, value=1.2, step=0.1)
        maintenance_rate = st.number_input("Annual Maintenance Cost (%)", min_value=0.0, value=1.0, step=0.1)
        insurance_monthly = st.number_input("Monthly Insurance ($)", min_value=0, value=100, step=10)
    
    with col4:
        appreciation_rate = st.number_input("Annual Home Appreciation (%)", min_value=0.0, value=3.0, step=0.1)
        time_horizon = st.number_input("Time Horizon (years)", min_value=1, value=10, step=1)

st.markdown('</div>', unsafe_allow_html=True)

# Calculations
buying_df = calculate_total_buying_cost(
    purchase_price,
    down_payment,
    annual_rate,
    years,
    property_tax_rate,
    maintenance_rate,
    insurance_monthly,
    appreciation_rate,
    time_horizon
)

renting_df = calculate_total_renting_cost(
    monthly_rent,
    rent_increase_rate,
    time_horizon
)

# Results Section
st.markdown('<div class="interior-section">', unsafe_allow_html=True)
st.header("Analysis Results")

# Key Metrics
col5, col6, col7 = st.columns(3)

with col5:
    monthly_mortgage = calculate_mortgage_payment(purchase_price - down_payment, annual_rate, years)
    st.metric("Monthly Mortgage Payment", f"${monthly_mortgage:,.2f}")

with col6:
    monthly_total = monthly_mortgage + (purchase_price * property_tax_rate / 1200) + (purchase_price * maintenance_rate / 1200) + insurance_monthly
    st.metric("Total Monthly Cost (Buying)", f"${monthly_total:,.2f}")

with col7:
    st.metric("Monthly Rent", f"${monthly_rent:,.2f}")

# Visualizations
st.plotly_chart(create_cost_comparison_chart(buying_df, renting_df), use_container_width=True)

col8, col9 = st.columns(2)

with col8:
    st.plotly_chart(
        create_monthly_breakdown_chart(
            monthly_mortgage,
            purchase_price * property_tax_rate / 1200,
            purchase_price * maintenance_rate / 1200,
            insurance_monthly
        ),
        use_container_width=True
    )

with col9:
    st.plotly_chart(create_equity_chart(buying_df), use_container_width=True)

# Breakeven Analysis
breakeven_month = calculate_breakeven_point(buying_df, renting_df)
if breakeven_month:
    st.info(f"Buying becomes cheaper than renting after {breakeven_month//12} years and {breakeven_month%12} months")
else:
    st.info("Renting remains cheaper throughout the analyzed period")

st.markdown('</div>', unsafe_allow_html=True)

# Considerations Section
st.markdown("""
<div class="modern-arch">
    <h2 style="color: white;">Additional Considerations</h2>
    <ul style="color: white;">
        <li>Market conditions and location factors</li>
        <li>Job stability and planned duration of stay</li>
        <li>Maintenance responsibilities</li>
        <li>Financial goals and investment preferences</li>
    </ul>
</div>
""", unsafe_allow_html=True)
