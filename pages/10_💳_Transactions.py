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
    return None

Statistics = get_data('Statistics')

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




















