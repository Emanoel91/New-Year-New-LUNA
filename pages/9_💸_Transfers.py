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
        st.metric(label='	Total Transfers Count(2023)', value=df['Total Transactions Count'])
with c3:
        st.metric(label='	Total Receivers Count', value=df['Total Transactions Count'])
with c4:
        st.metric(label='Total Senders Count', value=df['Total Senders Count']) 
