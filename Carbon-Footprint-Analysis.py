import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('carbon_footprint_data.csv')

# Display the first few rows of the dataset
print(data.head())

# Basic Analysis
total_emissions = data['CO2_Emissions_kg'].sum()
print(f"Total Carbon Footprint: {total_emissions} kg CO2")

# Breakdown by activity
activity_emissions = data.groupby('Activity')['CO2_Emissions_kg'].sum()
print(activity_emissions)

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(data['Activity'], data['CO2_Emissions_kg'], color='skyblue')
plt.xlabel('Activity')
plt.ylabel('CO2 Emissions (kg)')
plt.title('Carbon Footprint by Activity')
plt.xticks(rotation=45)
plt.show()

# Pie chart to show the proportion of each activity
plt.figure(figsize=(8, 8))
plt.pie(data['CO2_Emissions_kg'], labels=data['Activity'], autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Carbon Footprint by Activity')
plt.show()


Data set 

Activity,CO2_Emissions_kg
Electricity_Usage,50
Transportation_Car,30
Transportation_Plane,100
Food_Meat,40
Food_Vegetables,10
Waste_Plastic,15
Waste_Organic,5

 
