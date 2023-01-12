# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Addresses - New Year New LUNA', page_icon=':bar_chart:', layout='wide')
st.title('📱 Addresses')


# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# flipside API
@st.cache(ttl=600)
def get_data(query1):
    if query1 == 'Active Addresses':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/df33271b-7e1e-41bf-b7be-451fb308789b/data/latest')
    elif query1 == 'active address: statistic':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ca3eb8e1-5e55-4998-ab09-35a2b70293a2/data/latest')
    elif query1 == 'New Address':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6b26ebb2-3e6a-4c66-a8c4-7d7c4593b2d4/data/latest')
    elif query1 == 'new address: statistic':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0703a856-ad7d-49d3-a5e3-4aaf8efca476/data/latest')
    elif query1 == 'Total Addresses':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c7256259-9dae-492b-bc24-7f1b6e556065/data/latest')
    return None

Active_Addresses = get_data('Active Addresses')
active_address_statistic = get_data('active address: statistic')
New_Address = get_data('New Address')
new_address_statistic = get_data('new address: statistic')
Total_Addresses = get_data('Total Addresses')


df = Total_Addresses
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='Total Active Addresses (2023)', value=df['Total Active Addresses'])


df = Active_Addresses
fig = px.bar(df, x='Date', y='Active Addresses', title='Number of Avtive Addresses per Day', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Status', yaxis_title='Address Count', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = New_Address
fig = px.bar(df, x='Date', y='New Addresses', title='Number of New Addresses per Day', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Status', yaxis_title='Address Count', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = active_address_statistic
c1, c2 = st.columns(2)
with c1:
        fig = px.bar(df, x='Year', y='Average', color='Year', title='🟡 Daily Average Number of Active Addresses ')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='Year', y='Median', title='🟡 Daily Median Number of Active Addresses ')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
df = new_address_statistic
with c2:
        fig = px.bar(df, x='Year', y='Average', title='🟡 Daily Average Number of New Addresses ')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        
        fig = px.bar(df, x='Year', y='Median', title='🟡 Daily Median Number of New Addresses ')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.subheader('📃 Appendix')
st.write(
    """
**Active Address**:  An address is considered active as soon as it becomes a direct participant in a successful transaction.

**New Address**: A new address refers to an address that has recorded its first transaction.
    """
) 
