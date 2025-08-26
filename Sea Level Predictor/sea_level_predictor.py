import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read the sea level data from the CSV file into a DataFrame
    # The dataset contains yearly sea level measurements from 1880 onwards
    df = pd.read_csv('epa-sea-level.csv')

    # Create a new figure with a fixed size (10 inches wide, 6 inches tall)
    plt.figure(figsize=(10, 6))

    # Plot the original data as a scatter plot
    # x-axis: Year, y-axis: CSIRO Adjusted Sea Level
    # 'color' makes the points blue, 'alpha' controls transparency
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.6)

    # -----------------------------
    # First line of best fit (using ALL data from 1880 to latest available year)
    # -----------------------------

    # Perform linear regression on the full dataset
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create a range of years from 1880 through 2050 (for projecting into the future)
    years_extended = pd.Series(range(1880, 2051))

    # Compute predicted sea levels for each year using the regression line equation: y = slope*x + intercept
    line = slope * years_extended + intercept

    # Plot the regression line in red
    plt.plot(years_extended, line, 'r', label='1880-2050')

    # -----------------------------
    # Second line of best fit (using only data from the year 2000 onwards)
    # -----------------------------

    # Filter the dataset to include only years >= 2000
    df_recent = df[df['Year'] >= 2000]

    # Perform linear regression on the filtered data
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Create a range of years from 2000 through 2050 for the recent regression line
    years_recent_extended = pd.Series(range(2000, 2051))

    # Compute predicted sea levels for each year in the recent regression line
    line_recent = slope_recent * years_recent_extended + intercept_recent

    # Plot the second regression line in green
    plt.plot(years_recent_extended, line_recent, 'g', label='2000-2050')

    # -----------------------------
    # Final formatting of the chart
    # -----------------------------

    # Label the x-axis and y-axis
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Add a descriptive title
    plt.title('Rise in Sea Level')

    # Add a legend to distinguish between the two regression lines
    plt.legend()
        
    # Save the figure as 'sea_level_plot.png' (required for testing in FCC project)
    # and return the current Axes object for verification
    plt.savefig('sea_level_plot.png')
    return plt.gca()
