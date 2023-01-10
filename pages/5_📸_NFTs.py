# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='NFTs - New Year New LUNA', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('📸 NFTs')

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
    if query1 == 'Total Mint':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d0d103bd-88d9-4c74-b0d7-5f509cb4e675/data/latest')
    elif query1 == 'NFT Mint':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4454880f-7a76-4a64-9de7-41051b620905/data/latest')
    elif query1 == 'NFT Mint Statistics':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/933081b5-d83a-4ed8-bd92-db7f6b7c5bee/data/latest')
    elif query1 == 'Top 5 Collections Based on Mints Volume':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8c3794e7-0457-41d9-bce1-d36d4b068d1b/data/latest')
    elif query1 == 'Top 5 Collections Based on Mints Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/442de8f6-ddd9-4446-afaf-6c7d5ba347c3/data/latest')
    elif query1 == 'Top 5 Collections Based on Minters Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/62119110-38ff-4de3-a228-e0cc48ba0a42/data/latest')
    return None

Total_Mint = get_data('Total Mint')
NFT_Mint = get_data('NFT Mint')
NFT_Mint_Statistics = get_data('NFT Mint Statistics')
Top_5_Collections_Based_on_Mints_Volume = get_data('Top 5 Collections Based on Mints Volume')
Top_5_Collections_Based_on_Mints_Count = get_data('Top 5 Collections Based on Mints Count')
Top_5_Collections_Based_on_Minters_Count = get_data('Top 5 Collections Based on Minters Count')

st.subheader('✨ NFT Mints')

df = Total_Mint
c1, c2, c3 = st.columns(3)
    
with c1:
        st.metric(label='Total Volume:$LUNA (2023)', value=df['Total Volume'])
        st.metric(label='Total Number of Collections Minted (2023)', value=df['Total Collections'].round(2))
with c2:
        st.metric(label='Total Number of Mint (2023)', value=df['Total Mint'])
        st.metric(label='Total Number of NFT Minted (2023)', value=df['Total NFTs'].round(2))
with c3:
        st.metric(label='Total Number of Unique Minters (2023)', value=df['Total Minters'])
 
