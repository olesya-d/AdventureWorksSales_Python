# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# 1. Data preparation and aggregation

# Load the dataset
df = pd.read_csv("Q3\Data\Q3_Revenue-by-country.csv")

# Defining a list of offsets (x, y) to cycle through for better label placement.
OFFSETS = [
    (0, 10),    # Above the point
    (10, 0),    # To the right of the point
    (0, -20),   # Below the point
    (-10, 0),   # To the left of the point
    (30, 0),     # Top-Right
    (-10, 0)     # Top-Left
]

# 1.1. Aggregate data: Group the DataFrame by 'Country' and calculate the total
# number of stores (Store Count) and Total Revenue for each region.
stores_per_country = df.groupby('Country')['Store'].count()
total_revenue_by_country = df.groupby('Country')['Revenue'].sum()

# 1.2. Combine aggregated Series into a single DataFrame for plotting
plot_data = pd.DataFrame({
    'Total Revenue': total_revenue_by_country,
    'Store Count': stores_per_country
})

# 1.3. Calculate the correlation coefficient (Pearson) between Store Count and Total Revenue
correlation = plot_data['Store Count'].corr(plot_data['Total Revenue'])
print(f"\n--- Analysis Result ---")
print(
    f"Pearson Correlation (Store Count vs. Total Revenue): {correlation:.4f}")

# Print sorted data for review (sorted by Revenue, then Store Count)
print(plot_data.sort_values(
    by=["Total Revenue", "Store Count"], ascending=False))

# 2. Create scatter plot and Annotate

# 2.1. Set figure size
fig, ax = plt.subplots(figsize=(12, 7))

# 2.2. Create a scatter plot (Store Count vs. Total Revenue)
ax.scatter(
    x=plot_data['Store Count'],
    y=plot_data['Total Revenue'],
    s=100,  # Increased size for visibility
    alpha=0.7
)

# 2.3. Adding a trendline
# Calculate the linear regression (trendline)
# np.polyfit returns the coefficients [slope, intercept] of the best-fit line
z = np.polyfit(plot_data['Store Count'], plot_data['Total Revenue'], 1)
p = np.poly1d(z)  # Create a polynomial function from the coefficients

# Plot the trendline
ax.plot(
    plot_data['Store Count'],
    p(plot_data['Store Count']),
    color='red',
    linestyle='--',
    label=f'Trendline (R={correlation:.2f})'  # Add correlation to label
)

# 2.4. Cycle through the data to annotate each point with its country name
for i, (country, row) in enumerate(plot_data.iterrows()):

    # Get the offset position using the modulo operator (%)
    offset_index = i % len(OFFSETS)
    current_xytext = OFFSETS[offset_index]

    # Adjust horizontal alignment based on the chosen offset
    if current_xytext[0] > 0:
        ha_align = 'left'   # If shifting right, align text to the left
    elif current_xytext[0] < 0:
        ha_align = 'right'  # If shifting left, align text to the right
    else:
        ha_align = 'center'  # Default to center alignment

    # Annotate the plot with the country name
    ax.annotate(
        # Text: Use the country name (index)
        country,

        # Point coordinates: x=Store Count, y=Total Revenue
        (row['Store Count'], row['Total Revenue']),

        # Configuration settings:
        textcoords="offset points",  # Use the offset coordinate system
        xytext=current_xytext,       # Shift the text position cyclically
        ha=ha_align,                 # Adjust alignment dynamically
        fontsize=8,                  # Font size
        arrowprops=dict(
            arrowstyle="-",
            connectionstyle="arc3,rad=0.3",
            color="gray",
            alpha=0.3
        )
    )

# 3. Formatting and display

# 3.1. Formatting the Y-axis to display full numbers (no scientific notation)
formatter = StrMethodFormatter('{x:,.0f}')
ax.yaxis.set_major_formatter(formatter)

# 3.2. Set titles, labels, and grid
ax.set_title(
    'Relationship between Number of stores and Total Revenue by Country')
ax.set_xlabel('Number of Stores per Country')
ax.set_ylabel('Total Revenue')
ax.grid(True, linestyle='--', alpha=0.6)

# 3.3. Adjust layout to prevent labels from being cut off
plt.tight_layout()

# 3.4. Display the plot
plt.show()
