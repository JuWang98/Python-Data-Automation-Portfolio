import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Phase 1: Data Simulation (Mocking Client Data)
# ==========================================
# Creating a dummy dataset to simulate a client's messy CSV file
data = {
    'Product': ['iPhone', 'iPhone', 'iPad', 'MacBook', 'iPhone', 'iPad', 'Watch', 'MacBook'],
    'Price': [999, 999, 399, 2000, 999, 399, 300, 2000],
    'Sales': [1, 1, 2, 0, 1, 1, 5, None]  # Includes duplicates and missing values
}
# Save as CSV
df_initial = pd.DataFrame(data)
df_initial.to_csv('sales_data.csv', index=False)
print("✅ Simulation Data Generated: sales_data.csv")


# ==========================================
# Phase 2: Automation Script 
# ==========================================

print("\n=== 1. Data Loading ===")
# Load the dataset
try:
    df = pd.read_csv('sales_data.csv')
    print(f"Raw Data Loaded. Rows: {df.shape[0]}")
except FileNotFoundError:
    print("Error: File not found.")

print("\n=== 2. Data Cleaning (ETL) ===")
# 2.1 Handle Missing Values: Fill NaN sales with 0
df['Sales'] = df['Sales'].fillna(0)
# 2.2 Remove Duplicates
df = df.drop_duplicates()
print(f"Data Cleaned. Rows after cleaning: {df.shape[0]}")

print("\n=== 3. Data Analysis ===")
# Group by Product to calculate total sales
analysis = df.groupby('Product')['Sales'].sum()
print("Sales Performance by Product:")
print(analysis)

print("\n=== 4. Visualization ===")
# Plotting the Bar Chart
analysis.plot(kind='bar', title='Total Sales by Product', color='skyblue', edgecolor='black')
plt.xlabel('Product Name')
plt.ylabel('Total Sales Units')
plt.xticks(rotation=45) # Rotate labels for better readability
plt.tight_layout()      # Adjust layout to prevent clipping

print("\n=== 5. Delivery ===")
# Save the chart as an image file
output_filename = 'sales_report.png'
plt.savefig(output_filename)
print(f"✅ Chart saved successfully as: {output_filename}")

# Show plot (optional, for debugging)
plt.show()