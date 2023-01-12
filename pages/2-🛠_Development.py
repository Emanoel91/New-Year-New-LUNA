# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='Development - New Year New LUNA', page_icon=':bar_chart:', layout='wide')
st.title('🛠 Development')

# dash_style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# flipside API
@st.cache(ttl=600)
def get_data(query1):
    if query1 == 'Contracts':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4f470ff4-e192-4be3-94cf-dd143ca5f358/data/latest')
    elif query1 == 'Total Contracts':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e6f8b14f-ca91-42aa-9bd6-be3c56e5c33c/data/latest')
    elif query1 == 'Statistic Contracts':
              return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/744b7f5c-f0e5-41f4-ba4d-ad25a7e295a7/data/latest')
    return None

Contracts = get_data('Contracts')
Total_Contracts = get_data('Total Contracts')
Statistic_Contracts = get_data('Statistic Contracts')

df = Total_Contracts
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='Total Number of New Contracts (2023)', value=df['Total Contracts'])


df = Contracts
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Contracts'], name='New Contracts'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative Contracts'], name='Cummulative New Contracts'), secondary_y=True)
fig.update_layout(title_text='Number of New Contracts per Day')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


df = Statistic_Contracts
c1, c2 = st.columns(2)
with c1:
        fig = px.bar(df, x='Year', y='Average', title='🟡 Daily Average Number of New Contracts')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
               
with c2:
        fig = px.bar(df, x='Year', y='Median', title='🟡 Daily Median Number of New Contracts')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.subheader('📃 Appendix')
st.write(
    """
**Contract**:  A contract is self-executing code that carries out a set of instructions, which are then verified on the blockchain. These contracts are 
trustless, autonomous, decentralized, and transparent; they are irreversible and unmodifiable once deployed.
    """
) 
