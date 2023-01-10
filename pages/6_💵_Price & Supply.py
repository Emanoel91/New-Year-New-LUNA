# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Price & Supply - New Year New LUNA', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('💵 Price & Supply')

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
    elif query1 == 'NFT Sales ':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/1f27799c-8c17-4e3e-91bb-d7e955abbb46/data/latest')
    elif query1 == 'NFT Sales Statistic':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2a669fb4-18a7-4a0b-bad0-d5bb69e6dcd5/data/latest')
    elif query1 == 'Total NFT Sales':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/25404f65-67f4-4353-93ed-7d6b3105944c/data/latest')
    elif query1 == 'Top 5 Collections Count Based on Sales Volume($LUNA)':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/13231926-0148-401f-a588-1b53bde57479/data/latest')
    elif query1 == 'Top 5 Collections Count Based on Sales Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/777a3e5c-839f-4f18-89dc-053dd297c8e7/data/latest')
    elif query1 == 'Top 5 Collections Count Based on Sellers Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/db5daceb-922a-4f0a-aa96-d65b6c8eb866/data/latest')
    elif query1 == 'Top 5 Collections Count Based on Purchasers Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4dcf846b-e062-4b32-a3aa-24d9848076fc/data/latest')
    elif query1 == 'NFT Users Count':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6d19d5d2-d16d-4213-9269-14338523d4d5/data/latest')
    return None

Total_Mint = get_data('Total Mint')
NFT_Mint = get_data('NFT Mint')
NFT_Mint_Statistics = get_data('NFT Mint Statistics')
Top_5_Collections_Based_on_Mints_Volume = get_data('Top 5 Collections Based on Mints Volume')
Top_5_Collections_Based_on_Mints_Count = get_data('Top 5 Collections Based on Mints Count')
Top_5_Collections_Based_on_Minters_Count = get_data('Top 5 Collections Based on Minters Count')
NFT_Sales = get_data('NFT Sales ')
NFT_Sales_Statistic = get_data('NFT Sales Statistic')
Total_NFT_Sales = get_data('Total NFT Sales')
Top_5_Collections_Count_Based_on_Sales_Volume = get_data('Top 5 Collections Count Based on Sales Volume($LUNA)')
Top_5_Collections_Count_Based_on_Sales_Count = get_data('Top 5 Collections Count Based on Sales Count')
Top_5_Collections_Count_Based_on_Sellers_Count = get_data('Top 5 Collections Count Based on Sellers Count')
Top_5_Collections_Count_Based_on_Purchasers_Count = get_data('Top 5 Collections Count Based on Purchasers Count')
NFT_Users_Count = get_data('NFT Users Count')

st.subheader('✨ NFT Mints')
