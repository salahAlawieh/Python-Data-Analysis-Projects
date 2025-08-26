import pandas as pd
from typing import Dict, Any

def calculate_demographic_data(print_data: bool = True) -> Dict[str, Any]:
    """
    Analyze demographic data from the 'adult.data.csv' dataset.
    
    Calculates statistics such as race counts, average age of men, 
    percentage with Bachelors degree, income distribution based on education,
    minimum working hours, and country/occupation insights.
    
    Args:
        print_data (bool): If True, prints the analysis results.
        
    Returns:
        Dict[str, Any]: A dictionary containing calculated statistics.
    """
    # Define column names for the dataset
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 
        'marital-status', 'occupation', 'relationship', 'race', 
        'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 
        'native-country', 'salary'
    ]
    
    # Load dataset into a DataFrame
    df = pd.read_csv('adult.data.csv', skiprows=1, names=column_names)
    
    # Display first few rows to verify data
    print(df.head())
    
    # Count of each race represented in the dataset
    race_count = df['race'].value_counts()
    
    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    # Boolean masks for higher education and lower education
    higher_education_mask = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_mask = ~higher_education_mask
    
    # Percentage of people with higher education earning >50K
    higher_education_rich = round((df[higher_education_mask]['salary'] == '>50K').mean() * 100, 1)
    
    # Percentage of people without higher education earning >50K
    lower_education_rich = round((df[lower_education_mask]['salary'] == '>50K').mean() * 100, 1)
    
    # Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()
    
    # Percentage of rich among those who work minimum hours
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    rich_percentage = round(
        (df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] / num_min_workers) * 100
    )
    
    # Country with the highest percentage of people earning >50K
    country_stats = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)
    
    # Most popular occupation for those earning >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]
    
    # Optionally print results
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education earning >50K: {higher_education_rich}%")
        print(f"Percentage without higher education earning >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
    
    # Return all calculated statistics as a dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
