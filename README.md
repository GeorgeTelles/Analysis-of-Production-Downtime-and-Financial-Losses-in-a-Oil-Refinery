# Impact Analysis of Production Downtime and Financial Losses in a Oil Refinery

This project aims to analyze the impact of both scheduled and unscheduled downtime events on the production units of an oil refinery. The objective is to quantify the financial losses resulting from production decreases due to these downtimes, using historical data and impact estimates.

## Main Objectives of the Project:

### 1. Adjusted Production Analysis
The project begins by loading historical production data, downtime events, and operational costs from an Excel file. It adjusts the actual production of the refinery units, taking into account the impact of downtime events on operations.

### 2. Downtime Impact Simulation
For each downtime event recorded, the code calculates the reduction in oil production (in barrels per day - bpd) during the downtime period for the affected units. This simulation helps model how expected production is altered based on downtime events, avoiding negative production values.

### 3. Calculation of Financial Losses
Based on the price of a barrel of oil (set at $74 USD), the financial impact of downtime is calculated, reflecting the financial losses caused by the production decreases. This helps estimate the cost to the refinery due to downtime, aiding in decision-making and maintenance planning.

### 4. Data Visualization
The project generates two main visualizations:

- **Production Impact Graph**: Using Plotly, the project displays a timeline of expected and actual production, highlighting the impacts of downtimes. The graph allows a comparison of expected and actual production over time, with markers indicating the start and end dates of downtime events.
  
- **Financial Loss Graph**: A bar chart is generated to show the daily accumulated financial losses due to production downtime. This provides a clear visualization of when the largest financial losses occurred, aiding in the analysis of operational efficiency.

## Technologies Used:

- **Pandas**: For data manipulation and analysis of production, downtime events, and operational costs.
- **Plotly**: For creating interactive visualizations that help understand the impact of downtime on production and financial losses.
- **Excel (pandas.read_excel)**: For loading data from multiple sheets of an Excel file.

## Benefits of the Project:

- **Maintenance Planning**: The project provides a clear view of how downtime impacts production and refinery finances, allowing for better planning and prioritization of maintenance events.
  
- **Informed Decision-Making**: Financial losses are quantified and visualized, helping managers identify critical areas to improve production efficiency and reduce operational costs.
  
- **Production Optimization**: The analysis of downtimes and their financial impact, associating production changes, can guide the refinery in minimizing downtimes and optimizing production.

## Conclusion
In summary, this project offers a practical solution for analyzing the impact of downtime on oil production and finances in a refinery, using advanced data analysis and visualization tools to support strategic maintenance and operational decisions.
