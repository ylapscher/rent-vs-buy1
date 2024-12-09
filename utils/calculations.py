import numpy as np
import pandas as pd

def calculate_mortgage_payment(principal, annual_rate, years):
    """Calculate monthly mortgage payment."""
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    return principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)

def calculate_total_buying_cost(
    purchase_price,
    down_payment,
    annual_rate,
    years,
    property_tax_rate,
    maintenance_rate,
    insurance_monthly,
    appreciation_rate,
    time_horizon
):
    """Calculate total cost of buying over time."""
    monthly_mortgage = calculate_mortgage_payment(
        purchase_price - down_payment,
        annual_rate,
        years
    )
    
    monthly_property_tax = (purchase_price * property_tax_rate / 100) / 12
    monthly_maintenance = (purchase_price * maintenance_rate / 100) / 12
    
    monthly_costs = monthly_mortgage + monthly_property_tax + monthly_maintenance + insurance_monthly
    
    # Calculate appreciation
    future_value = purchase_price * (1 + appreciation_rate/100)**time_horizon
    
    # Create monthly breakdown
    months = range(1, time_horizon * 12 + 1)
    df = pd.DataFrame(index=months)
    
    df['Monthly_Cost'] = monthly_costs
    df['Cumulative_Cost'] = df['Monthly_Cost'].cumsum()
    df['Property_Value'] = [purchase_price * (1 + appreciation_rate/100)**(i/12) for i in months]
    df['Equity'] = df['Property_Value'] - (purchase_price - down_payment)
    
    return df

def calculate_total_renting_cost(
    monthly_rent,
    rent_increase_rate,
    time_horizon
):
    """Calculate total cost of renting over time."""
    months = range(1, time_horizon * 12 + 1)
    df = pd.DataFrame(index=months)
    
    df['Monthly_Cost'] = [monthly_rent * (1 + rent_increase_rate/100)**(i/12) for i in months]
    df['Cumulative_Cost'] = df['Monthly_Cost'].cumsum()
    df['Equity'] = 0
    
    return df

def calculate_breakeven_point(buying_df, renting_df):
    """Calculate when buying becomes cheaper than renting."""
    diff_df = buying_df['Cumulative_Cost'] - renting_df['Cumulative_Cost']
    breakeven_month = diff_df[diff_df < 0].index[0] if len(diff_df[diff_df < 0]) > 0 else None
    return breakeven_month
