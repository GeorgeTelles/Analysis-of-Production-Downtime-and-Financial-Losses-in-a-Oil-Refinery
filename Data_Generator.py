import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Creating data for Production Units
production_units = pd.DataFrame({
    'unit_id': [1, 2, 3],
    'unit_name': ['Paulínia Refinery', 'Duque de Caxias Refinery', 'Capuava Refinery'],
    'daily_capacity_bpd': [200000, 150000, 100000],
    'current_efficiency': [0.95, 0.92, 0.90],
    'operational_status': ['Operational', 'Operational', 'Operational'],
    'installation_date': ['2005-07-12', '2010-05-20', '2015-08-15']
})

# Creating data for Production History
dates = pd.date_range(start='2024-01-01', periods=250, freq='D')
productions = []
for date in dates:
    for i, row in production_units.iterrows():
        actual_production = row['daily_capacity_bpd'] * row['current_efficiency'] * np.random.uniform(0.95, 1.05)
        productions.append([date.date(), row['unit_id'], int(actual_production)])

production_history = pd.DataFrame(productions, columns=['date', 'unit_id', 'actual_production_bpd'])

# Creating data for Scheduled and Unscheduled Shutdowns
shutdowns = pd.DataFrame({
    'shutdown_id': [1, 2, 3, 4],
    'unit_id': [1, 2, 1, 3],
    'shutdown_type': ['Scheduled', 'Unscheduled', 'Scheduled', 'Unscheduled'],
    'start_date': ['2024-03-10', '2024-02-20', '2024-04-05', '2024-02-25'],
    'end_date': ['2024-03-15', '2024-02-22', '2024-04-10', '2024-02-27'],
    'reason': ['Preventive maintenance', 'Mechanical failure', 'Mandatory inspection', 'Electrical failure'],
    'estimated_impact_bpd': [20000, 50000, 15000, 30000]
})

# Creating data for Operational Costs and Losses
costs = pd.DataFrame({
    'cost_id': [1, 2, 3, 4],
    'unit_id': [1, 2, 3, 1],
    'cost_type': ['Maintenance', 'Production Loss', 'Emergency Repair', 'Production Loss'],
    'date': ['2024-03-10', '2024-02-20', '2024-02-25', '2024-04-05'],
    'value_usd': [150000, 500000, 80000, 300000]
})

# Creating data for Maintenance Events
maintenance_events = pd.DataFrame({
    'event_id': [1, 2, 3, 4],
    'unit_id': [1, 2, 3, 1],
    'maintenance_type': ['Preventive', 'Corrective', 'Emergency', 'Preventive'],
    'planned_date': ['2024-03-10', '2024-02-20', '2024-02-25', '2024-04-05'],
    'duration_days': [5, 2, 3, 6],
    'status': ['Confirmed', 'Executed', 'Executed', 'Planned']
})

with pd.ExcelWriter('refinery_shutdown_simulation.xlsx', engine='openpyxl') as writer:
    production_units.to_excel(writer, sheet_name='Production_Units', index=False)
    production_history.to_excel(writer, sheet_name='Production_History', index=False)
    shutdowns.to_excel(writer, sheet_name='Shutdowns', index=False)
    costs.to_excel(writer, sheet_name='Operational_Costs', index=False)
    maintenance_events.to_excel(writer, sheet_name='Maintenance_Events', index=False)

print("Excel file created successfully: refinery_shutdown_simulation.xlsx")