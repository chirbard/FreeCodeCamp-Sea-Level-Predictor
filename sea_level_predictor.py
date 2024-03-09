import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # print(df.head())

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(x, y)
    x_start = x[0]
    x_end = 2051
    x_new = pd.Series(range(x_start, x_end))
    plt.plot(x_new, intercept + slope*x_new, 'r', label='fitted line')

    # Create second line of best fit
    index_2000 = x[x == 2000].index[0]
    x_new = x[index_2000:]
    y_new = y[index_2000:]
    # print(y_new)

    slope, intercept, r, p, se = linregress(x_new, y_new)
    x_start = 2000
    x_end = 2051
    x_new = pd.Series(range(x_start, x_end))
    # print(x_new)
    plt.plot(x_new, intercept + slope*x_new, 'g')



    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()