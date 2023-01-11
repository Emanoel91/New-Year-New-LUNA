# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Transfers - New Year New LUNA', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('💸 Transfers')

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
    if query1 == 'LUNA Transfers':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b8139ea6-2c16-4073-a55d-13db530d01b6/data/latest')
    elif query1 == 'Total Transfers Data':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/41f518da-9a93-4559-b832-94cf4b0b3b3a/data/latest')
    elif query1 == 'Average & Median Transfers Data':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/bec2bf74-52c9-4562-8fc9-5856ea397868/data/latest')
    return None

LUNA_Transfers = get_data('LUNA Transfers')
Total_Transfers_Data = get_data('Total Transfers Data')
Average_Median_Transfers_Data = get_data('Average & Median Transfers Data')

st.subheader('🟡 LUNA Transfers Overview')
df = Total_Transfers_Data
c1, c2, c3, c4 = st.columns(4)
    
with c1:
        st.metric(label='Total Transfers Volume(2023)', value=df['Total Transfers Volume'])
with c2:
        st.metric(label='Total Transfers Count(2023)', value=df['Total Transfers Count'])
with c3:
        st.metric(label='Total Receivers Count(2023)', value=df['Total Receivers Count'])
with c4:
        st.metric(label='Total Senders Count(2023)', value=df['Total Senders Count'])
  
df = LUNA_Transfers
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Transfers Volume'], name='Transfers Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative Transfers Volume'], name='Cummulative Transfers Volume'), secondary_y=True)
fig.update_layout(title_text='Transfers Volume per Day')
fig.update_yaxes(title_text='$LUNA', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = LUNA_Transfers
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Transfers Count'], name='Transfers Count'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative Transfers Count'], name='Cummulative Transfers Count'), secondary_y=True)
fig.update_layout(title_text='Transfers Count per Day')
fig.update_yaxes(title_text='Transfers', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = LUNA_Transfers
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df['Date'], y=df['Senders Count'], name='Senders Count'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Receivers Count'], name='Receivers Count'), secondary_y=True)
fig.update_layout(title_text='Number of LUNA Senders & Receivers')
fig.update_yaxes(title_text='Addresses', secondary_y=False)
fig.update_yaxes(title_text='Addresses', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


df = Average_Median_Transfers_Data
c1, c2= st.columns(2)
with c1:
       fig = px.bar(df, x='Year', y='Average Transfers Volume', color='Year', title='Average Daily Transfers Volume', log_y=False')
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Year', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
       fig = px.bar(df, x='Year', y='Average Transfers Count', color='Year', title='Average Daily Transfers Count', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Year', yaxis_title='Transfers', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly) 

c1, c2= st.columns(2)
with c1:
       fig = px.bar(df, x='Year', y='Average Senders Count', color='Year', title='Average Daily Senders Count', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Year', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
with c2:
       fig = px.bar(df, x='Year', y='Average Receivers Count', color='Year', title='Average Daily Receivers Count', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Year', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  

c1, c2= st.columns(2)
with c1:
       fig = px.bar(df, x='Year', y='Median Transfers Volume', color='Year', title='Median Daily Transfers Volume', log_y=False')
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Year', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
       fig = px.bar(df, x='Year', y='Median Transfers Count', color='Year', title='Median Daily Transfers Count', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Year', yaxis_title='Transfers', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly) 

c1, c2= st.columns(2)
with c1:
       fig = px.bar(df, x='Year', y='Median Senders Count', color='Year', title='Median Daily Senders Count', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Year', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
with c2:
       fig = px.bar(df, x='Year', y='Median Receivers Count', color='Year', title='Median Daily Receivers Count', log_y=False)
       fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Year', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
       st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
