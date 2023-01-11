# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Swap - New Year New LUNA', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('🔄 Swap')

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
    if query1 == 'Buyers Data':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fb61a268-50f2-4771-9f1e-9a922d690026/data/latest')
    elif query1 == 'Sellers Data':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d1d47747-7382-45c5-b8e2-b767bc80d668/data/latest')
    elif query1 == 'Number of New Pools':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/40832512-00b9-4467-a307-e4c8f46d8159/data/latest')
    elif query1 == 'Average and Median Swap':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/91201621-6905-4c4d-b517-40b31fafbfdf/data/latest')
    elif query1 == 'Average and Median Swappers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e3ed4d67-c7c8-4180-a122-b4d60ff6e836/data/latest')
    elif query1 == 'Swap Actions':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0ccc6374-10ac-400a-9dd6-e812739ba14c/data/latest')
    elif query1 == 'Swappers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3581a525-11b6-4f95-bc86-2d3cb82bd112/data/latest')
    return None

Buyers_Data = get_data('Buyers Data')
Sellers_Data = get_data('Sellers Data')
Number_of_New_Pools = get_data('Number of New Pools')
Average_and_Median_Swap = get_data('Average and Median Swap')
Average_and_Median_Swappers = get_data('Average and Median Swappers')
Swap_Actions = get_data('Swap Actions')
Swappers = get_data('Swappers')

st.subheader('LUNA Swap Overview')
c1, c2, c3 = st.columns(3)
df = Buyers_Data
with c1:
        st.metric(label='Total Buying Volume:$LUNA (2023)', value=df['Total Buying Volume'])
with c2:
        st.metric(label='Total Buying Count(2023)', value=df['Total Buying Count'])
with c3:
        st.metric(label='Total Buyers Count(2023)', value=df['Total Buyers Count'])
  
c1, c2, c3 = st.columns(3)
df = Sellers_Data
with c1:
        st.metric(label='Total Selling Volume:$LUNA (2023)', value=df['Total Selling Volume'])
with c2:
        st.metric(label='Total Selling Count(2023)', value=df['Total Selling Count'])
with c3:
        st.metric(label='Total Sellers Count(2023)', value=df['Total Sellers Count'])  
  
c1, c2, c3 = st.columns(3)
df = Number_of_New_Pools  
with c1:
        st.metric(label='Total Number of New Pools(2023)', value=df['Total Number of New Pools'])

df = Swap_Actions
fig = px.bar(df, x='Date', y='Volume', color='Action', title='Total Swap Volume per Day', log_y=True)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Action', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = go.Figure()
for i in df['Action'].unique():
    fig.add_trace(go.Scatter(
        name=i,
        x=df.query("Action == @i")['Date'],
        y=df.query("Action == @i")['Volume'],
        mode='bar',
        stackgroup='one',
        groupnorm='percent'
     ))
fig.update_layout(title='Status of Swaps Volume(%Normalized)')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)






