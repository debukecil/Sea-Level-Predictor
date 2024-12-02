import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

    # Create first line of best fit (using all data)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    line_all = slope * years_extended + intercept
    plt.plot(years_extended, line_all, color='red', label='Fit: 1880-2050')

    # Create second line of best fit (using data from 2000)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    line_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, line_recent, color='green', label='Fit: 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
