# 🏠 Rent vs. Buy Calculator

An interactive web application that helps users make informed decisions about whether to rent or buy a property. This comprehensive calculator provides detailed financial analysis and visualizations to compare the long-term costs and benefits of renting versus buying a home.

## Purpose

The calculator is designed for:
- Prospective homebuyers evaluating their options
- Real estate professionals advising clients
- Financial planners helping with housing decisions
- Anyone interested in understanding the financial implications of renting vs. buying

## ✨ Features

### Financial Calculations
- Monthly mortgage payment computation
- Property tax estimates
- Maintenance cost projections
- Insurance cost integration
- Down payment considerations

### Interactive Visualizations
- Cost comparison charts showing cumulative expenses over time
- Monthly payment breakdown pie charts
- Home equity growth visualization
- Breakeven point analysis

### Advanced Configurations
- Customizable property appreciation rates
- Adjustable rent increase scenarios
- Flexible time horizon settings
- Detailed maintenance and tax rate options

### Comparison Tools
- Side-by-side cost analysis
- Breakeven point calculation
- Equity building visualization
- Monthly cost breakdown

## 🛠 Technical Details

### Built With
- [Streamlit](https://streamlit.io/) - The web application framework
- [Plotly](https://plotly.com/) - Interactive visualization library
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [NumPy](https://numpy.org/) - Numerical computations

### Calculation Methodologies
- Mortgage calculations using standard amortization formulas
- Property value appreciation using compound growth
- Rent increases modeled with annual percentage growth
- Total cost analysis incorporating all monthly expenses

## 🚀 Setup Instructions

### Dependencies
```bash
streamlit
plotly
pandas
numpy
```

### Installation
1. Clone the repository
2. Install the required packages:
```bash
pip install streamlit plotly pandas numpy
```

### Running the Application
1. Navigate to the project directory
2. Run the Streamlit application:
```bash
streamlit run main.py
```

### Configuration
- Server settings can be modified in `.streamlit/config.toml`
- Custom styling available in `styles/custom.css`
- Default values can be adjusted in `main.py`

## 📖 Usage Guide

### Input Parameters

#### Basic Options
- **Purchase Price**: Total cost of the property
- **Down Payment**: Initial payment amount
- **Mortgage Rate**: Annual interest rate
- **Mortgage Term**: Length of the mortgage in years
- **Monthly Rent**: Current rental payment
- **Rent Increase Rate**: Expected annual increase in rent

#### Advanced Options
- **Property Tax Rate**: Annual property tax as a percentage
- **Maintenance Cost**: Expected annual maintenance as a percentage
- **Insurance**: Monthly insurance premium
- **Home Appreciation**: Expected annual property value increase
- **Time Horizon**: Analysis period in years

### Understanding Results

The calculator provides:
1. Monthly payment comparisons between buying and renting
2. Interactive charts showing cumulative costs over time
3. Visual breakdown of monthly homeownership costs
4. Equity growth projections
5. Breakeven analysis showing when buying becomes more economical than renting

### Advanced Features
- Adjustable time horizons for long-term analysis
- Customizable appreciation and inflation rates
- Detailed cost breakdown visualizations
- Mobile-responsive design
- Real-time calculation updates

## 📊 Screenshots
[To be added: Screenshots of the calculator in action]

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

## 📝 License
[To be added: License information]
