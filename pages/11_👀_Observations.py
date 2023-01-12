# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Staking - New Year New LUNA', page_icon=':bar_chart:', layout='wide')
st.title('🩸 Staking')
