import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
population_df = pd.read_csv('dataset/world_population.csv')
happiness_df = pd.read_csv('dataset/world-happiness-report-2021.csv')

# Set the title of the Streamlit app
st.title('🌍 Global Population & Happiness Dashboard 😊')

# Sidebar for page selection
page = st.sidebar.selectbox('Select a page', ['World Population Statistics 📊', 'World Happiness Report 😊'])

if page == 'World Population Statistics 📊':
    # Display the dataframe
    st.write('### 🌍 World Population Data', population_df)

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
    .st-emotion-cache-1espb9k a {
        color: rgb(234, 237, 240);
        text-decoration: none;
    }
    .sidebar .sidebar-content a:hover {
        color: rgb(210, 165, 125);
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('<a href="#population-growth-rate">📈 Population Growth Rate</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="#population-density">🏙️ Population Density</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="#correlation-matrix">📊 Correlation Matrix</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="#insights-from-the-data">🔍 Insights from the Data</a>', unsafe_allow_html=True)

    # Filter data based on user input
    country_data = population_df[population_df['Country/Territory'] == selected_country]

    # Display selected country data
    st.write(f'### 🌍 Population Data for {selected_country}', country_data)

    # Reshape the DataFrame for plotting
    years = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']
    population_data = country_data.melt(id_vars=['Country/Territory'], value_vars=years, var_name='Year', value_name='Population')
    population_data['Year'] = population_data['Year'].str.extract('(\d{4})').astype(int)

    # Calculate population density for each year
    for year in years:
        population_data.loc[population_data['Year'] == int(year.split()[0]), 'Density (per km²)'] = population_data['Population'] / country_data['Area (km²)'].values[0]

    # Plotting
    st.write('<h2 id="population-growth-rate"> Population Growth Rate</h2>', unsafe_allow_html=True)
    plt.figure(figsize=(12, 5), facecolor='#262730')
    ax = sns.lineplot(data=population_data, x='Year', y='Population', color='blue')
    ax.set_facecolor('#262730')
    ax.set_title(f'Population of {selected_country} Over the Years', color='white')
    ax.set_xlabel('Year', color='white')
    ax.set_ylabel('Population', color='white')
    ax.tick_params(colors='white')
    st.pyplot(plt)

    st.write('<h2 id="population-density"> Population Density</h2>', unsafe_allow_html=True)
    plt.figure(figsize=(10, 5), facecolor='#262730')
    ax = sns.barplot(data=population_data, x='Year', y='Density (per km²)', color='blue')
    ax.set_facecolor('#262730')
    ax.set_title(f'Population Density of {selected_country}', color='white')
    ax.set_xlabel('Year', color='white')
    ax.set_ylabel('Density (per km²)', color='white')
    ax.tick_params(colors='white')
    st.pyplot(plt)

    # Correlation heatmap
    st.write('<h2 id="correlation-matrix"> Correlation Matrix</h2>', unsafe_allow_html=True)
    correlation = population_df[['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']].corr()
    plt.figure(figsize=(10, 8), facecolor='#262730')
    ax = sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    ax.set_facecolor('#262730')
    ax.set_title('Correlation Matrix', color='white')
    ax.tick_params(colors='white')
    st.pyplot(plt)

    # Insights section
    st.write('<h2 id="insights-from-the-data">Insights from the Data</h2>', unsafe_allow_html=True)

    st.write('### 📈 Population Growth Trends')
    st.write('By examining the line plot of population over the years, you can identify trends in population growth for the selected country. For example, you might observe periods of rapid growth, stability, or decline.')

    st.write('### 🏙️ Population Density Changes')
    st.write('The bar plot of population density over the years can reveal how densely populated the country has become over time. You can compare the density values across different years to understand how population distribution has changed relative to the country\'s area.')

    st.write('### 📊 Correlation Analysis')
    st.write('The correlation matrix heatmap provides insights into the relationships between different variables. For example:')
    st.write('- A strong positive correlation between `Growth Rate` and `World Population Percentage` might indicate that countries with higher growth rates contribute more significantly to the world\'s population.')
    st.write('- A strong negative correlation between `Density (per km²)` and `Area (km²)` might suggest that larger countries tend to have lower population densities.')

    st.write('### 🌍 Country-Specific Insights')
    st.write('By selecting different countries from the sidebar, you can compare their population statistics. This can help identify unique patterns or anomalies specific to certain countries.')

    st.write('### 📜 Historical Population Data')
    st.write('The reshaped DataFrame with population data for different years allows you to analyze historical population changes. You can identify significant events or policies that might have influenced population growth or decline during specific periods.')

    st.write('### 📈 Growth Rate Analysis')
    st.write('The line plot of growth rate over the years can help you understand how the growth rate has fluctuated. You can identify periods of high growth and investigate potential causes, such as economic development, immigration, or birth rates.')

    st.write('### 🏙️ Density and Urbanization')
    st.write('The population density plot can provide insights into urbanization trends. Higher population densities might indicate increased urbanization, while lower densities could suggest more rural or sparsely populated areas.')

elif page == 'World Happiness Report 😊':
    # Display the dataframe
    st.write('### 😊 World Happiness Report Data', happiness_df)

    # Sidebar for user input
    st.sidebar.header('User Input')
    selected_country = st.sidebar.selectbox('Select a country', happiness_df['Country name'].unique())

    # Filter data based on user input
    country_data = happiness_df[happiness_df['Country name'] == selected_country]

    # Display selected country data
    st.write(f'### 😊 Happiness Data for {selected_country}', country_data)
    
    # Sidebar links with styling
    st.sidebar.markdown('## Navigation')
    st.sidebar.markdown("""
    <style>
    .sidebar .sidebar-content {
        font-size: 18px;
    }
    .st-emotion-cache-1espb9k a {
        color: rgb(234, 237, 240);
        text-decoration: none;
    }
    .sidebar .sidebar-content a:hover {
        color: rgb(210, 165, 125);
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('<a href="#population-growth-rate">😊 Happiness Score</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="#population-density">😊 Happiness Factors</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="#correlation-matrix">📊 Correlation Matrix</a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="#insights-from-the-data">🔍 Insights from the Data</a>', unsafe_allow_html=True)

    # Plotting
    st.write('<h2 id="happiness-score">Happiness Score</h2>', unsafe_allow_html=True)
    plt.figure(figsize=(10, 5), facecolor='#262730')
    ax = sns.barplot(data=country_data, x='Country name', y='Ladder score', color='blue')
    ax.set_facecolor('#262730')
    ax.set_title(f'Happiness Score of {selected_country}', color='white')
    ax.set_xlabel('Country', color='white')
    ax.set_ylabel('Happiness Score', color='white')
    ax.tick_params(colors='white')
    st.pyplot(plt)

    st.write('<h2 id="happiness-factors">Happiness Factors</h2>', unsafe_allow_html=True)
    factors = ['Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']
    plt.figure(figsize=(10, 5), facecolor='#262730')
    ax = sns.barplot(data=country_data.melt(id_vars=['Country name'], value_vars=factors, var_name='Factor', value_name='Score'), x='Factor', y='Score', color='blue')
    ax.set_facecolor('#262730')
    ax.set_title(f'Happiness Factors for {selected_country}', color='white')
    ax.set_xlabel('Factor', color='white')
    ax.set_ylabel('Score', color='white')
    ax.tick_params(colors='white')
    st.pyplot(plt)

    # Correlation heatmap
    st.write('<h2 id="correlation-matrix"> Correlation Matrix</h2>', unsafe_allow_html=True)
    correlation = happiness_df[['Ladder score', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']].corr()
    plt.figure(figsize=(10, 8), facecolor='#262730')
    ax = sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    ax.set_facecolor('#262730')
    ax.set_title('Correlation Matrix', color='white')
    ax.tick_params(colors='white')
    st.pyplot(plt)

    # Insights section
    st.write('<h2 id="insights-from-the-data">Insights from the Data</h2>', unsafe_allow_html=True)

    st.write('### Happiness Score Trends 😊 ')
    st.write('By examining the bar plot of happiness scores, you can identify the overall happiness score for the selected country.')

    st.write('### Happiness Factors Analysis 😊 ')
    st.write('The bar plot of happiness factors can reveal which factors contribute most to the happiness score of the selected country. You can compare the scores of different factors to understand their impact.')

    st.write('### 🌍 Country-Specific Insights')
    st.write('By selecting different countries from the sidebar, you can compare their happiness statistics. This can help identify unique patterns or anomalies specific to certain countries.')

    st.write('### 📜 Historical Happiness Data')
    st.write('The reshaped DataFrame with happiness data for different years allows you to analyze historical happiness changes. You can identify significant events or policies that might have influenced happiness during specific periods.')

    st.write('### 📊 Correlation Analysis')
    st.write('From correlation analysis to understand the relationships between different happiness factors and the overall happiness score. This can provide insights into which factors are most strongly associated with happiness.')