import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
population_df = pd.read_csv('dataset/world_population.csv')
happiness_df = pd.read_csv('dataset/world-happiness-report-2021.csv')

# Set the title of the Streamlit app
st.title('World Statistics Dashboard')

# Sidebar for page selection
page = st.sidebar.selectbox('Select a page', ['World Population Statistics', 'World Happiness Report'])

if page == 'World Population Statistics':
    # Display the dataframe
    st.write('### World Population Data', population_df)

    # Sidebar for user input
    st.sidebar.header('User Input')
    selected_country = st.sidebar.selectbox('Select a country', population_df['Country/Territory'].unique())

    # Sidebar links with styling
    st.sidebar.markdown('## Navigation')
    st.sidebar.markdown("""
    <style>
    .sidebar .sidebar-content {
        font-size: 18px;
    }
    a {
        color: #1f77b4;
        text-decoration: none;
    }
    a:hover {
        color: #ff7f0e;
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('[Population Growth Rate](#population-growth-rate)')
    st.sidebar.markdown('[Population Density](#population-density)')
    st.sidebar.markdown('[Correlation Matrix](#correlation-matrix)')
    st.sidebar.markdown('[Insights from the Data](#insights-from-the-data)')

    # Filter data based on user input
    country_data = population_df[population_df['Country/Territory'] == selected_country]

    # Display selected country data
    st.write(f'### Population Data for {selected_country}', country_data)

    # Reshape the DataFrame for plotting
    years = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']
    population_data = country_data.melt(id_vars=['Country/Territory'], value_vars=years, var_name='Year', value_name='Population')
    population_data['Year'] = population_data['Year'].str.extract('(\d{4})').astype(int)

    # Calculate population density for each year
    for year in years:
        population_data.loc[population_data['Year'] == int(year.split()[0]), 'Density (per km²)'] = population_data['Population'] / country_data['Area (km²)'].values[0]

    # Plotting
    st.write('### Population Growth Rate')
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=population_data, x='Year', y='Population')
    plt.title(f'Population of {selected_country} Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Population')
    st.pyplot(plt)

    st.write('### Population Density')
    plt.figure(figsize=(10, 5))
    sns.barplot(data=population_data, x='Year', y='Density (per km²)')
    plt.title(f'Population Density of {selected_country}')
    plt.xlabel('Year')
    plt.ylabel('Density (per km²)')
    st.pyplot(plt)

    # Correlation heatmap
    st.write('### Correlation Matrix')
    correlation = population_df[['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix')
    st.pyplot(plt)

    # Insights section
    st.write('## Insights from the Data')

    st.write('### Population Growth Trends')
    st.write('By examining the line plot of population over the years, you can identify trends in population growth for the selected country. For example, you might observe periods of rapid growth, stability, or decline.')

    st.write('### Population Density Changes')
    st.write('The bar plot of population density over the years can reveal how densely populated the country has become over time. You can compare the density values across different years to understand how population distribution has changed relative to the country\'s area.')

    st.write('### Correlation Analysis')
    st.write('The correlation matrix heatmap provides insights into the relationships between different variables. For example:')
    st.write('- A strong positive correlation between `Growth Rate` and `World Population Percentage` might indicate that countries with higher growth rates contribute more significantly to the world\'s population.')
    st.write('- A strong negative correlation between `Density (per km²)` and `Area (km²)` might suggest that larger countries tend to have lower population densities.')

    st.write('### Country-Specific Insights')
    st.write('By selecting different countries from the sidebar, you can compare their population statistics. This can help identify unique patterns or anomalies specific to certain countries.')

    st.write('### Historical Population Data')
    st.write('The reshaped DataFrame with population data for different years allows you to analyze historical population changes. You can identify significant events or policies that might have influenced population growth or decline during specific periods.')

    st.write('### Growth Rate Analysis')
    st.write('The line plot of growth rate over the years can help you understand how the growth rate has fluctuated. You can identify periods of high growth and investigate potential causes, such as economic development, immigration, or birth rates.')

    st.write('### Density and Urbanization')
    st.write('The population density plot can provide insights into urbanization trends. Higher population densities might indicate increased urbanization, while lower densities could suggest more rural or sparsely populated areas.')

elif page == 'World Happiness Report':
    # Display the dataframe
    st.write('### World Happiness Report Data', happiness_df)

    # Sidebar for user input
    st.sidebar.header('User Input')
    selected_country = st.sidebar.selectbox('Select a country', happiness_df['Country name'].unique())

    # Filter data based on user input
    country_data = happiness_df[happiness_df['Country name'] == selected_country]

    # Display selected country data
    st.write(f'### Happiness Data for {selected_country}', country_data)
    
    # Sidebar links with styling
    st.sidebar.markdown('## Navigation')
    st.sidebar.markdown("""
    <style>
    .sidebar .sidebar-content {
        font-size: 18px;
    }
    a {
        color: #1f77b4;
        text-decoration: none;
    }
    a:hover {
        color: #ff7f0e;
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('[Happiness Score](#population-growth-rate)')
    st.sidebar.markdown('[Happiness Factors](#population-density)')
    st.sidebar.markdown('[Correlation Matrix](#correlation-matrix)')
    st.sidebar.markdown('[Insights from the Data](#insights-from-the-data)')

    # Plotting
    st.write('### Happiness Score')
    plt.figure(figsize=(10, 5))
    sns.barplot(data=country_data, x='Country name', y='Ladder score')
    plt.title(f'Happiness Score of {selected_country}')
    plt.xlabel('Country')
    plt.ylabel('Happiness Score')
    st.pyplot(plt)

    st.write('### Happiness Factors')
    factors = ['Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']
    plt.figure(figsize=(10, 5))
    sns.barplot(data=country_data.melt(id_vars=['Country name'], value_vars=factors, var_name='Factor', value_name='Score'), x='Factor', y='Score')
    plt.title(f'Happiness Factors for {selected_country}')
    plt.xlabel('Factor')
    plt.ylabel('Score')
    st.pyplot(plt)

    # Correlation heatmap
    st.write('### Correlation Matrix')
    correlation = happiness_df[['Ladder score', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix')
    st.pyplot(plt)

    # Insights section
    st.write('## Insights from the Data')

    st.write('### Happiness Score Trends')
    st.write('By examining the bar plot of happiness scores, you can identify the overall happiness score for the selected country.')

    st.write('### Happiness Factors Analysis')
    st.write('The bar plot of happiness factors can reveal which factors contribute most to the happiness score of the selected country. You can compare the scores of different factors to understand their impact.')

    st.write('### Country-Specific Insights')
    st.write('By selecting different countries from the sidebar, you can compare their happiness statistics. This can help identify unique patterns or anomalies specific to certain countries.')

    st.write('### Historical Happiness Data')
    st.write('The reshaped DataFrame with happiness data for different years allows you to analyze historical happiness changes. You can identify significant events or policies that might have influenced happiness during specific periods.')

    st.write('### Correlation Analysis')
    st.write('You can perform correlation analysis to understand the relationships between different happiness factors and the overall happiness score. This can provide insights into which factors are most strongly associated with happiness.')