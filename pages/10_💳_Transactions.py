# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Transactions - New Year New LUNA', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('💳 Transactions')

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
    if query1 == 'Statistics':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6ed60ef6-b640-4fb9-a720-1104d909734f/data/latest')
    elif query1 == 'Transactions Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d2ab8450-d214-4fc4-90a8-b6b258c4c573/data/latest')
    elif query1 == 'Transactions Status':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d3605635-4543-4b5d-af72-61bcbdae439e/data/latest')     
    elif query1 == 'Transactions':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b0cbd7ce-9ccb-4fed-b4e3-524def997fb8/data/latest')  
    elif query1 == 'Max/Avg/Median/Min Transaction Fees':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e5ffdad3-6d81-4589-920d-00d4c4caed6c/data/latest')
    elif query1 == 'Average':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4fe93470-7960-4541-ab91-eb6e5e90a9d5/data/latest')     
    return None

Statistics = get_data('Statistics')
Transactions_Count = get_data('Transactions Count')
Transactions_Status = get_data('Transactions Status')
Transactions = get_data('Transactions')
Max_Avg_Median_Min_Transaction_Fees = get_data('Max/Avg/Median/Min Transaction Fees')
Average = get_data('Average')

df = Statistics
c1, c2, c3 = st.columns(3)
with c1:
        st.metric(label='Total Transactions Count(2023)', value=df['Total TXs Count'])
        st.metric(label='Average TPM(2023)', value=df['Average TPM'])  
        st.metric(label='Average TX per Block(2023)', value=df['Average TX per Block'])    
with c2:
        st.metric(label='Total Blocks Count(2023)', value=df['Total Blocks Count'])
        st.metric(label='Average TX Fee(2023)', value=df['Average TX Fee'])        
with c3: 
        st.metric(label='Total TX Fees:$LUNA(2023)', value=df['Total TX Fee'])
        st.metric(label='Average TX per Wallet(2023)', value=df['Average TX per Wallet'])    
   
df = Transactions_Count
fig = px.bar(df, x='Date', y='TXs Count', color='Success', title='Number of Transactions per Day', log_y=False)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Success', yaxis_title='TXs', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Transactions_Count
fig = px.bar(df, x='Date', y='TX Fee', color='Success', title='Total Transaction Fees per Day', log_y=False)
fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Success', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
   
with c1:
      df = Transactions_Status  
      fig = px.pie(df, values='TXs Count', names='Success', title='Share of Transactions(2023)')
      fig.update_layout(legend_title='Success', legend_y=0.5)
      fig.update_traces(textinfo='percent+label', textposition='inside')
      st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
      
      fig = px.bar(df, x='Success', y='TXs Count', color='Success', title='Total Transactions Count(2023)', log_y=False)
      fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Success', yaxis_title='TXs', xaxis={'categoryorder':'total ascending'})
      st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
      df = Transactions_Status  
      fig = px.pie(df, values='TX Fee', names='Success', title='Share of Transaction Fees(2023)')
      fig.update_layout(legend_title='Success', legend_y=0.5)
      fig.update_traces(textinfo='percent+label', textposition='inside')
      st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
      
      fig = px.bar(df, x='Success', y='TX Fee', color='Success', title='Total Transaction Fees(2023)', log_y=False)
      fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Success', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
      st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)     

df = Transactions
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['TXs Count'], name='TXs Count'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Blocks Count'], name='Blocks Count'), secondary_y=True)
fig.update_layout(title_text='Number of Transactions & Blocks per Day')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Transactions
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['TX per Wallet'], name='TX per Wallet'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['TX per Block'], name='TX per Block'), secondary_y=False)
fig.update_layout(title_text='Number of Transactions per Wallet & per Block')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Transactions
fig = px.bar(df, x='Date', y='TX Fee', title='Total Transaction Fees per Day', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = px.bar(df, x='Date', y='TPM', title='Daily TPM', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Max_Avg_Median_Min_Transaction_Fees
fig = px.line(df, x='Date', y='Fee', color='Metric', title='Max/Avg/Median/Min Transaction Fees', log_y=True)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Average
c1, c2, c3= st.columns(3)
with c1:
       fig = px.bar(df, x='Year', y='Average TXs Count', color='Year', title='Daily Average TXs Count', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
with c2:
       fig = px.bar(df, x='Year', y='Average Blocks Count', color='Year', title='Daily Average Blocks Count', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='Blocks', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c3:
       fig = px.bar(df, x='Year', y='Average TX Fee', color='Year', title='Daily Average TX Fee', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2, c3= st.columns(3)
with c1:
       fig = px.bar(df, x='Year', y='Average TX per Block', color='Year', title='Daily Average TX per Block', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
with c2:
       fig = px.bar(df, x='Year', y='Average TX per Wallet', color='Year', title='Daily Average TX per Wallet', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c3:
       fig = px.bar(df, x='Year', y='Average TPM', color='Year', title='Daily Average TPM', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)











