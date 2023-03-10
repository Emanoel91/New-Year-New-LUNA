# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Swap - New Year New LUNA', page_icon=':bar_chart:', layout='wide')
st.title('🔄 Swap')



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
    elif query1 == 'Total':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/859ea2b8-d532-43b7-9ef1-8cd91a46c77a/data/latest')
    elif query1 == 'Status of Swappers Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/65e1d0f7-c8fc-421d-8178-b40ab38c0ec2/data/latest')
    elif query1 == 'Total Swappers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e3e8878e-4b4d-4d83-9a3f-4ca5584e67ea/data/latest')
    return None

Buyers_Data = get_data('Buyers Data')
Sellers_Data = get_data('Sellers Data')
Number_of_New_Pools = get_data('Number of New Pools')
Average_and_Median_Swap = get_data('Average and Median Swap')
Average_and_Median_Swappers = get_data('Average and Median Swappers')
Swap_Actions = get_data('Swap Actions')
Swappers = get_data('Swappers')
Total = get_data('Total')
Status_of_Swappers_Count = get_data('Status of Swappers Count')
Total_Swappers = get_data('Total Swappers')

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
fig = px.bar(df, x='Date', y='Volume', color='Action', title='Total Swap Volume per Day (Log Scale)', log_y=True)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Action', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
df = Swap_Actions
with c1:
  fig = go.Figure()
  for i in df['Action'].unique():
      fig.add_trace(go.Scatter(
          name=i,
          x=df.query("Action == @i")['Date'],
          y=df.query("Action == @i")['Volume'],
          mode='lines',
          stackgroup='one',
          groupnorm='percent'
       ))
  fig.update_layout(title='Status of Swaps Volume(%Normalized)')
  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
  df = Total  
  fig = px.pie(df, values='Total Volume', names='Action', title='Total Swaps Volume')
  fig.update_layout(legend_title='Action', legend_y=0.5)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
  
# --------------------------------------------------------------------------------------------------------------------

df = Swap_Actions
fig = px.bar(df, x='Date', y='Transactions Count', color='Action', title='Total Swaps Count per Day', log_y=False)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Action', yaxis_title='TXs', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
df = Swap_Actions
with c1:
  fig = go.Figure()
  for i in df['Action'].unique():
      fig.add_trace(go.Scatter(
          name=i,
          x=df.query("Action == @i")['Date'],
          y=df.query("Action == @i")['Transactions Count'],
          mode='lines',
          stackgroup='one',
          groupnorm='percent'
       ))
  fig.update_layout(title='Status of Swaps Count(%Normalized)')
  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
  
with c2:
  df = Total  
  fig = px.pie(df, values='Total Transactions Count', names='Action', title='Total Number of Swaps')
  fig.update_layout(legend_title='Action', legend_y=0.5)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Swappers
fig = px.bar(df, x='Date', y='Users Count', color='User Type', title='Total Number of Swappers per Day', log_y=False)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Action', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
df = Status_of_Swappers_Count
with c1:
  fig = go.Figure()
  for i in df['Type'].unique():
      fig.add_trace(go.Scatter(
          name=i,
          x=df.query("Type == @i")['Date'],
          y=df.query("Type == @i")['Users Count'],
          mode='lines',
          stackgroup='one',
          groupnorm='percent'
       ))
  fig.update_layout(title='Status of Swappers Count(%Normalized)')
  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
  
  
df = Total_Swappers
with c2:
 
   
  fig = px.pie(df, values='Total Users Count', names='User Type', title='Total Number of Swappers')
  fig.update_layout(legend_title='User Type', legend_y=0.5)
  fig.update_traces(textinfo='percent+label', textposition='inside')
  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
  
  
df = Average_and_Median_Swap
c1, c2, c3= st.columns(3)
with c1:
       fig = px.bar(df, x='Action', y='Average Volume', color='Year', title='Average Daily Swaps volume(2023)', log_y=False, barmode='group')
       fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Year', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
       fig = px.bar(df, x='Action', y='Median Volume', color='Year', title='Median Daily Swaps volume(2023)', log_y=False, barmode='group')
       fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Year', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)    
with c2:
       fig = px.bar(df, x='Action', y='Average Transactions Count', color='Year', title='Average Daily Swaps Count(2023)', log_y=False, barmode='group')
       fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Year', yaxis_title='TXs', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
       fig = px.bar(df, x='Action', y='Median Transactions Count', color='Year', title='Median Daily Swaps Count(2023)', log_y=False, barmode='group')
       fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Year', yaxis_title='TXs', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)    
df = Average_and_Median_Swappers
c1, c2= st.columns(2)
with c3:
       fig = px.bar(df, x='User Type', y='Average Users Count', color='Year', title='Average Daily Swappers Count(2023)', log_y=False, barmode='group')
       fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Year', yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
       fig = px.bar(df, x='User Type', y='Median Users Count', color='Year', title='Median Daily Swappers Count(2023)', log_y=False, barmode='group')
       fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Year', yaxis_title='Swappers', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)        

st.subheader('📃 Appendix')
st.write(
    """
**Swapping**: Crypto swapping allows users to instantly trade one cryptocurrency for another, with no crypto-to-fiat exchange required. Saving time and paying less 
in fees are obvious benefits, but it’s far from the only reason users participate in swapping. Crypto tokens are effectively the keys to their native blockchain’s 
kingdom, affording holders various benefits within their ecosystems. Token holders may have the opportunity to vote on community governance proposals that guide the 
future of a project or stake their share in exchange for passive interest income. Swapping makes it easier for crypto users to explore the further reaches of the 
blockchain, and be a part of multiple projects they wish to support.
    """
) 

