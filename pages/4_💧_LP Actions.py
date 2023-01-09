# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='LP Actions - New Year New LUNA', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('💧 LP Actions')

# Cover
c1 , c2 = st.columns(2)

#c1.image(Image.open('Images/transactions.JPG'))

#with c2: 
#        st.subheader('📄 ***List of contents***')
 #       st.write(
  #                  """
   #                 1️⃣ **Overview**
             
    #                2️⃣ **Daily Transactions**
            
     #               3️⃣ **Activity of Addresses**
            
      #              4️⃣ **Transaction Fees**
       #             """
        #          )

# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# flipside API
@st.cache(ttl=600)
def get_data(query1):
    if query1 == 'Liquidity pools':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cac60939-7270-4b4c-ada5-c47dbb3350ec/data/latest')
    elif query1 == 'Liquidity pools statistic Average':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8f667e4d-f334-4e6a-9426-1b7dfccf08c2/data/latest')
    elif query1 == 'Liquidity pools statistic Median':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ead7df54-8d50-414b-bc27-f75e51900f3e/data/latest')
    elif query1 == 'Total Transactions Count of each Action':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/236f33de-dcc6-4dc1-875f-4dde90250398/data/latest')
    elif query1 == 'User Type':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5bf044f7-a81c-4aee-a565-57e9231956a0/data/latest')
    elif query1 == 'Average Daily Liquidity Providers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ae7f585b-58cd-40e9-aaca-e5d116fde30e/data/latest')
    elif query1 == 'Median Daily Liquidity Providers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2b17d842-e3a2-4c2e-ac75-6656d9fd836b/data/latest')
    elif query1 == 'Number of New Liquidity Providers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7f7a1fe1-4eac-4a03-9fda-bc0f5e029f1b/data/latest')
    elif query1 == 'Total New Liquidity Providers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7ad5a1fd-f041-4e39-b5d2-9a1a994070ae/data/latest')
    return None

Liquidity_pools = get_data('Liquidity pools')
Liquidity_pools_statistic_Average = get_data('Liquidity pools statistic Average')
Liquidity_pools_statistic_Median = get_data('Liquidity pools statistic Median')
Total_Transactions_Count_of_each_Action = get_data('Total Transactions Count of each Action')
User_Type = get_data('User Type')
Average_Daily_Liquidity_Providers = get_data('Average Daily Liquidity Providers')
Median_Daily_Liquidity_Providers = get_data('Median Daily Liquidity Providers')
Number_of_New_Liquidity_Providers = get_data('Number of New Liquidity Providers')
Total_New_Liquidity_Providers = get_data('Total New Liquidity Providers')

df = Total_New_Liquidity_Providers
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='Total Number of New Liquidity Providers (2023)', value=df['New Liquidity Providers'])

df = Liquidity_pools
fig = px.bar(df, x='Date', y='Transactions Count', color='Action', title='Number of Actions per Day', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)

with c1:      
        df = Liquidity_pools_statistic_Average
        fig = px.bar(df, x='Action', y='Average Tx Count', color='Year', title='Daily Average Number of Actions', log_y=False, barmode='group')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
              
with c2:
        df = Liquidity_pools_statistic_Median
        fig = px.bar(df, x='Action', y='Median Tx Count', color='Year', title='Daily Median Number of Actions', log_y=False, barmode='group')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)    


df = Total_Transactions_Count_of_each_Action
c1, c2 = st.columns(2) 
with c1:
        fig = px.pie(df, values='Total Transactions Count', names='Action', title='Total Transactions Count of each Action')
        fig.update_layout(legend_title='Action', legend_y=0.5)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)    
with c2:
       fig = px.bar(df, x='Action', y='Total Transactions Count', color='Action', title='', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Class', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
    
df = User_Type
fig = px.bar(df, x='Date', y='Addresses', color='User Type', title='Number of Users per Day', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Addresses Count', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

   
df = Number_of_New_Liquidity_Providers 
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['New Liquidity Providers'], name='Liquidity Providers'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative New Liquidity Providers'], name='Cummulative Liquidity Providers'), secondary_y=True)
fig.update_layout(title_text='Number of New Liquidity Providers')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Average_Daily_Liquidity_Providers
c1, c2 = st.columns(2)

with c1:      
        fig = px.bar(df, x='User Type', y='Average Address Count', color='Year', title='Daily Average Number of Liquidity Providers', log_y=False, barmode='group')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Liquidity Providers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = Median_Daily_Liquidity_Providers        
with c2:
        fig = px.bar(df, x='User Type', y='Median Address Count', color='Year', title='Daily Median Number of Liquidity Providers', log_y=False, barmode='group')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Liquidity Providers', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
 
 
 
       


