from preswald import text, plotly, connect, get_df, query
import plotly.express as px

# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df('EV_Population_Data_csv')

# UI Intro
text('# EV Market Trends & Insights')
text('Exploring EV adoption trends, brand dominance, and vehicle performance using real-world data from WaTech.')

## Analysis 1: Most Popular EV Models
sql1 = 'SELECT Make, Model, COUNT(*) as Total_Count FROM EV_Population_Data GROUP BY Make, Model ORDER BY COUNT(*) DESC LIMIT 20'
popular_ev_df = query(sql1, 'EV_Population_Data')
fig1 = px.bar(popular_ev_df, x='Model', y='Total_Count', color='Make', title='Top 20 EV Models by Popularity', text_auto=True)
plotly(fig1)

## Analysis 2: Market Share of Top 20 EV Brands
sql2 = 'SELECT Make, COUNT(*) as Total_Count FROM EV_Population_Data GROUP BY Make ORDER BY Total_Count DESC LIMIT 20'
brand_share_df = query(sql2, 'EV_Population_Data')
fig2 = px.pie(brand_share_df, values='Total_Count', names='Make', title='EV Market Share by Top 20 Manufacturers')
plotly(fig2)

## Analysis 3: Which EVs Have the Best Range?
sql3 = 'SELECT Make, Model, AVG(Range) as Avg_Range FROM EV_Population_Data WHERE Range > 0 GROUP BY Make, Model ORDER BY Avg_Range DESC LIMIT 20'
best_range_df = query(sql3, 'EV_Population_Data')
fig3 = px.bar(best_range_df, x='Make', y='Avg_Range', color='Model', title='Top 20 EV Models with Best Battery Range', text_auto=True)
plotly(fig3)

## --- Analysis 4: Distribution of EV Model Years on the Road ---
sql4 = 'SELECT Model_Year, COUNT(*) as Total_Registrations FROM EV_Population_Data GROUP BY Model_Year ORDER BY Model_Year ASC'
ev_growth_df = query(sql4, 'EV_Population_Data')
fig4 = px.line(ev_growth_df, x='Model_Year', y='Total_Registrations', title='Distribution of EV Model Years on the Road', markers=True)
plotly(fig4)

## --- Analysis 5: Market Share by Year ---
sql5 = 'SELECT Model_Year, Make, COUNT(*) as Total_Count FROM EV_Population_Data WHERE Model_Year >= 2010GROUP BY Model_Year, Make ORDER BY Model_Year ASC, Total_Count DESC'
yearly_share_df = query(sql5, 'EV_Population_Data')
fig5 = px.line(yearly_share_df, x='Model_Year', y='Total_Count', color='Make', title='EV Manufacturer Market Share Since 2010', markers=True)
plotly(fig5)