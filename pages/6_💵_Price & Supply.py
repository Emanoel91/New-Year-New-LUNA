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

st.subheader('💰 LUNA Price')
df = Current_LUNA_Price
c1, c2 = st.columns(2)
    
with c1:
        st.metric(label='**Current LUNA Price**', value=df['CLOSE'])
df = Percentage_of_LUNA_price_changes_in_2023
with c2:
        st.metric(label='**Percentage of LUNA Price Changes in 2023**', value=df['Percentage of Changes'])

df = LUNA_Price_per_Day
fig = px.line(df, x='Day', y='Price', color='Criteria', title='LUNA Price per Day', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = LUNA_Price_Metric
fig = px.line(df, x='Day', y='Price', color='TYPE', title='LUNA Price Metric', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Range_of_Price_Change
fig = px.bar(df, x='Day', y='RoPC', title='Range of Price Changes(RoPC)', log_y=False)
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Comparison_of_LUNA_price_metrics_in_2022_and_2023
fig = px.bar(df, x='Criteria', y='Amount', color='Year', title='Comparison of LUNA price metrics in 2022 and 2023', log_y=False, barmode='group')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.subheader('🟡 LUNA Supply')
df = Current_Circulating_Supply 
c1, c2, c3 = st.columns(3)

with c1:
        st.metric(label='**Total Supply**', value=df['Total Supply'])
with c2:
        st.metric(label='**Circulating Supply**', value=df['Circulating Supply'])
with c3:
        st.metric(label='**%Circulating Supply Ratio**', value=df['%Circulating Supply Ratio'])
  
df = Circulating_Supply 
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Circulating Supply'], name='Circulating Supply'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['%Circulating Supply Ratio'], name='%Circulating Supply Ratio'), secondary_y=False)
fig.update_layout(title_text='Circulating Supply per Day')
fig.update_yaxes(title_text='$LUNA', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
