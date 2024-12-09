import plotly.graph_objects as go
import plotly.express as px

def create_cost_comparison_chart(buying_df, renting_df):
    """Create interactive cost comparison chart."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=buying_df.index,
        y=buying_df['Cumulative_Cost'],
        name='Buying',
        line=dict(color='#4A4036', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=renting_df.index,
        y=renting_df['Cumulative_Cost'],
        name='Renting',
        line=dict(color='#8B7355', width=2)
    ))
    
    fig.update_layout(
        title='Cumulative Cost Comparison',
        xaxis_title='Months',
        yaxis_title='Total Cost ($)',
        template='simple_white',
        hovermode='x unified'
    )
    
    return fig

def create_monthly_breakdown_chart(monthly_mortgage, monthly_tax, monthly_maintenance, monthly_insurance):
    """Create pie chart showing monthly payment breakdown."""
    labels = ['Mortgage', 'Property Tax', 'Maintenance', 'Insurance']
    values = [monthly_mortgage, monthly_tax, monthly_maintenance, monthly_insurance]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=.3,
        marker_colors=['#4A4036', '#8B7355', '#A67F5D', '#C4A484']
    )])
    
    fig.update_layout(
        title='Monthly Payment Breakdown',
        template='simple_white'
    )
    
    return fig

def create_equity_chart(buying_df):
    """Create equity growth visualization."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=buying_df.index,
        y=buying_df['Equity'],
        name='Home Equity',
        fill='tozeroy',
        line=dict(color='#4A4036', width=2)
    ))
    
    fig.update_layout(
        title='Home Equity Growth Over Time',
        xaxis_title='Months',
        yaxis_title='Equity ($)',
        template='simple_white',
        showlegend=False
    )
    
    return fig
