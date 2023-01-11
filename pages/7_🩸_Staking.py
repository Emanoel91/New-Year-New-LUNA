# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Staking - New Year New LUNA', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('🩸 Staking')

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
    if query1 == 'Staking':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/aaa4ec8e-e4fb-4750-aa81-5ea6f8ebe42e/data/latest')
    elif query1 == 'New Delegators':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fe40ef40-b9a9-4e46-a9de-94ac3f7c34e3/data/latest')
    elif query1 == 'Average Data':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5efdda3f-ab5d-4be0-a153-285ca79afbcc/data/latest')
    elif query1 == 'Median Data':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/be444c96-df64-450d-92bd-42cd490bbab9/data/latest')
    elif query1 == 'Top 5 Validators Based Delegations Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4557eb21-e024-4146-adf3-6a5eb7c69532/data/latest')
    elif query1 == 'Number of Delegations on Top Validators':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6681e7c6-b66e-4532-be3b-8bbd333f8db1/data/latest')
    elif query1 == 'Top 5 Validators Based Delegations Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/702c782e-cd12-4609-b29f-36e6445a684c/data/latest')
    elif query1 == 'Volume of Delegations on Top Validators':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/314509fa-fcb9-46b1-a0f6-375279bc357c/data/latest')
    elif query1 == 'Top 5 Validators Based Delegators Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e73903ca-50f9-4d91-a15d-8e74dbb48175/data/latest')
    elif query1 == 'Number of Delegators on Top Validators':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f355c76a-7778-4e80-87b0-ec8c24a666f9/data/latest')
    elif query1 == 'Total Actions':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b32a5716-bf03-43f1-a1c6-d6b6710f101c/data/latest')
    elif query1 == 'Top 30 Validators and Delegations':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/33fbefbd-cdcc-44bf-83f9-cd622e95a569/data/latest')
    elif query1 == 'Top 30 Validators and Undelegations':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2dfeff1c-a3e3-4a34-8093-6028ccdb2331/data/latest')
    elif query1 == 'Top 30 Validators and Redelegations':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/619b6a48-984c-444f-9a32-4756c14eff7c/data/latest')
    return None

Staking = get_data('Staking')
New_Delegators = get_data('New Delegators')
Average_Data = get_data('Average Data')
Median_Data = get_data('Median Data')
Top_5_Validators_Based_Delegations_Count = get_data('Top 5 Validators Based Delegations Count')
Number_of_Delegations_on_Top_Validators = get_data('Number of Delegations on Top Validators')
Top_5_Validators_Based_Delegations_Volume = get_data('Top 5 Validators Based Delegations Volume')
Volume_of_Delegations_on_Top_Validators = get_data('Volume of Delegations on Top Validators')
Top_5_Validators_Based_Delegators_Count = get_data('Top 5 Validators Based Delegators Count')
Number_of_Delegators_on_Top_Validators = get_data('Number of Delegators on Top Validators')
Total_Actions = get_data('Total Actions')
Top_30_Validators_and_Delegations = get_data('Top 30 Validators and Delegations')
Top_30_Validators_and_Undelegations = get_data('Top 30 Validators and Undelegations')
Top_30_Validators_and_Redelegations = get_data('Top 30 Validators and Redelegations')

df = Total_Actions
c1, c2, c3 = st.columns(3)
with c1:
       fig = px.bar(df, x='ACTION', y='Total Users Count', color='ACTION', title='Total Users Count (2023)', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='ACTION', yaxis_title='', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
       fig = px.bar(df, x='ACTION', y='Total Amount', color='ACTION', title='Total Amount (2023)', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='ACTION', yaxis_title='', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly) 
with c3: 
       fig = px.bar(df, x='ACTION', y='Total Transactions Count', color='ACTION', title='Total Transactions Count (2023)', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='ACTION', yaxis_title='', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
df = Staking
fig = px.bar(df, x='Date', y='Volume', color='ACTION', title='Total Volume per Day', log_y=False)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='ACTION', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
  
fig = px.bar(df, x='Date', y='Action Count', color='ACTION', title='Total Transactions Count per Day', log_y=False)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='ACTION', yaxis_title='', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
  
fig = px.bar(df, x='Date', y='Addresses Count', color='User Type', title='Total Users Count per Day', log_y=False)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='ACTION', yaxis_title='', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
  

fig = px.bar(df, x='Date', y='Validators Count', color='ACTION', title='Total Validators Count per Day', log_y=False)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='ACTION', yaxis_title='', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  

df = New_Delegators
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['New Delegators'], name='New Delegators'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative New Delegators'], name='Cummulative New Delegators'), secondary_y=True)
fig.update_layout(title_text='Number of New Delegators per Day (2023)')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
  
df = Average_Data
c1, c2, c3 = st.columns(3)
with c1:
       fig = px.bar(df, x='Action', y='Average Volume', color='Year', title='Average Volume of each Action', log_y=False, barmode='group')
       fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Action', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
 
  
  
  
