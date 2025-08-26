import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Load the data and parse dates, using 'date' as the index
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data by removing outliers outside the 2.5th and 97.5th percentiles
df = df[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot() -> plt.Figure:
    """
    Draw a line plot of daily forum page views over time.
    
    Returns:
        matplotlib.figure.Figure: Figure object containing the line plot.
    """
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], 'r-', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save figure
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot() -> plt.Figure:
    """
    Draw a bar plot showing average monthly page views per year.
    
    Returns:
        matplotlib.figure.Figure: Figure object containing the bar plot.
    """
    # Copy and prepare data
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    
    # Aggregate average page views by year and month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Rename columns to month names
    df_bar.columns = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
    
    # Create bar plot
    fig = df_bar.plot(kind='bar', figsize=(10, 8)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    
    return fig

def draw_box_plot() -> plt.Figure:
    """
    Draw box plots to visualize yearly trends and monthly seasonality of page views.
    
    Returns:
        matplotlib.figure.Figure: Figure object containing the box plots.
    """
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    
    # Define correct order for months
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot for seasonality
    sns.boxplot(
        x='month',
        y='value',
        data=df_box.sort_values('month_num'),
        order=month_order,
        ax=axes[1]
    )
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    plt.tight_layout()
    
    # Save figure
    fig.savefig('box_plot.png')
    
    return fig

# Example usage:
line_fig = draw_line_plot()
bar_fig = draw_bar_plot()
box_fig = draw_box_plot()
