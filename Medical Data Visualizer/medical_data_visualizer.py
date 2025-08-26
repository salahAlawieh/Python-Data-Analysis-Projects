import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from typing import Any

# Load the medical dataset
df = pd.read_csv('medical_examination.csv')
print("First few rows of the dataset:")
print(df.head())

# 1. Add an 'overweight' column based on BMI > 25
df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).astype(int)

# 2. Normalize 'cholesterol' and 'gluc' columns: 0 = normal, 1 = above normal
df['cholesterol'] = df['cholesterol'].map({1: 0, 2: 1, 3: 1})
df['gluc'] = df['gluc'].map({1: 0, 2: 1, 3: 1})

def draw_cat_plot() -> Any:
    """
    Create a categorical bar plot showing counts of health indicators 
    split by cardiovascular disease status.
    
    Returns:
        matplotlib.figure.Figure: Figure object containing the catplot.
    """
    # Convert data to long format for categorical plotting
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    
    # Group and count occurrences of each feature by cardio status
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # Rename 'value' column for clarity
    df_cat = df_cat.rename(columns={'value': 'feature_value'})
    
    # Create the categorical plot using seaborn
    catplot = sns.catplot(
        x='variable',
        y='total',
        hue='feature_value',
        col='cardio',
        data=df_cat,
        kind='bar',
        height=5,
        aspect=1.2,
        palette='Set2'
    )
    
    # Customize plot appearance
    catplot.set_axis_labels("Health Indicators", "Total Count")
    catplot.set_titles("Cardiovascular Disease: {col_name}")
    catplot.set_xticklabels(rotation=45)
    catplot.fig.suptitle(
        'Distribution of Health Indicators by Cardiovascular Disease Status', 
        y=1.05, fontsize=16, fontweight='bold'
    )
    
    # Optional: Add value labels on top of bars
    for ax in catplot.axes.flat:
        for container in ax.containers:
            ax.bar_label(container, fmt='%.0f', padding=3, fontsize=9)
    
    plt.tight_layout()
    plt.show()
    
    # Save figure to file
    catplot.fig.savefig('catplot.png')
    
    return catplot.fig

def draw_heat_map() -> Any:
    """
    Create a heatmap of the correlation matrix for cleaned medical data.
    
    Returns:
        matplotlib.figure.Figure: Figure object containing the heatmap.
    """
    # Filter out extreme values and incorrect blood pressure readings
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle (to hide redundant correlations)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Draw the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        cmap='icefire',
        center=0,
        square=True,
        cbar_kws={'shrink': 0.8},
        ax=ax
    )
    
    # Save figure to file
    fig.savefig('heatmap.png')
    
    return fig

# Example usage:
cat_fig = draw_cat_plot()
heat_fig = draw_heat_map()
