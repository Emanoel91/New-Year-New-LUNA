# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Observations - New Year New LUNA', page_icon=':bar_chart:', layout='wide')
st.title('👀 Observations')




df = Current_LUNA_Price
c1, c2 = st.columns(2)
    
with c1:
       st.write(
       """
      🔴 Metrics that Increased in 2023 
       """
         )
with c2:
         st.write(
         """
         🟢 Metrics that Increased in 2023 
         """
          )  
