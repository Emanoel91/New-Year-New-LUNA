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
    if query1 == 'Current LUNA Price':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/be07fc87-6d9e-4706-bf89-0aab3fb5fb9e/data/latest')
    elif query1 == 'Percentage of LUNA price changes in 2023':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eb503870-b936-4e9d-9901-1a69b0dfc935/data/latest')
    elif query1 == 'LUNA Price per Day':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b7677888-8e5e-45da-b593-be145726fdac/data/latest')
    elif query1 == 'Range of Price Change':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/80d32a13-1075-4592-bd4a-088251135465/data/latest')
    elif query1 == 'LUNA Price Metric':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b265c317-afc6-47b7-91fa-893d5f368988/data/latest')
    elif query1 == 'Comparison of LUNA price metrics in 2022 and 2023':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5f1b8942-57b2-4fe9-87dd-2210db99ac16/data/latest')
    elif query1 == 'Circulating Supply':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/dd621ea9-27f5-489d-9b14-4f3990955e94/data/latest')
    elif query1 == 'Current Circulating Supply ':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7ae6ccd1-535c-49cc-b84b-d4815f0a2dbf/data/latest')
    return None

Current_LUNA_Price = get_data('Current LUNA Price')
Percentage_of_LUNA_price_changes_in_2023 = get_data('Percentage of LUNA price changes in 2023')
LUNA_Price_per_Day = get_data('LUNA Price per Day')
Range_of_Price_Change = get_data('Range of Price Change')
LUNA_Price_Metric = get_data('LUNA Price Metric')
Comparison_of_LUNA_price_metrics_in_2022_and_2023 = get_data('Comparison of LUNA price metrics in 2022 and 2023')
Circulating_Supply = get_data('Circulating Supply')
Current_Circulating_Supply = get_data('Current Circulating Supply ')
