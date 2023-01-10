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
    if query1 == '':
              return pd.read_json('')
    elif query1 == '':
              return pd.read_json('')
    elif query1 == '':
              return pd.read_json('')
    elif query1 == '':
              return pd.read_json('')
    elif query1 == '':
              return pd.read_json('')
    elif query1 == '':
              return pd.read_json('')
    elif query1 == '':
              return pd.read_json('')
    elif query1 == '':
              return pd.read_json('')
    return None

11 = get_data('11')
11 = get_data('11')
11 = get_data('11')
11 = get_data('11')
11 = get_data('11')
11 = get_data('11')
11 = get_data('11')
11 = get_data('11')

st.subheader('💰 LUNA Price')

st.subheader('🟡 LUNA Supply')
