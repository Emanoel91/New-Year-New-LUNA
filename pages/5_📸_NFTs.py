# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

theme_plotly = None # None or streamlit

# Structure
st.set_page_config(page_title='NFTs - New Year New LUNA', page_icon=':bar_chart:', layout='wide')
st.title('📸 NFTs')

st.subheader('📃 definitions')
st.write(
    """
**1️⃣ NFT**: NFT means non-fungible tokens (NFTs), which are generally created using the same type of programming used for cryptocurrencies. In simple terms these 
cryptographic assets are based on blockchain technology. 

**2️⃣ Minting: Minting an NFT, or non-fungible token, is publishing a unique digital asset on a blockchain.
    """
)

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

df = Total_Mint
c1, c2, c3 = st.columns(3)
    
with c1:
        st.metric(label='**Total Volume:$LUNA (2023)**', value=df['Total Volume'])
        st.metric(label='**Total Number of Collections Minted (2023)**', value=df['Total Collections'].round(2))
with c2:
        st.metric(label='**Total Number of Mint (2023)**', value=df['Total Mint'])
        st.metric(label='**Total Number of NFT Minted (2023)**', value=df['Total NFTs'].round(2))
with c3:
        st.metric(label='**Total Number of Unique Minters (2023)**', value=df['Total Minters'])
  
df = NFT_Mint

fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'], name='Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative Volume'], name='Cummulative Volume'), secondary_y=True)
fig.update_layout(title_text='Volume of NFTs Minted per Day')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Mint'], name='Mint'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative Mint'], name='Cummulative Mint'), secondary_y=True)
fig.update_layout(title_text='Number of Transactions Related to Mint')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Minters'], name='Minters'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative Minters'], name='Cummulative Minters'), secondary_y=True)
fig.update_layout(title_text='Number of Unique Minters per Day')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['NFTs'], name='NFTs'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative NFTs'], name='Cummulative NFTs'), secondary_y=True)
fig.update_layout(title_text='Number of NFTs Minted per Day')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Collections'], name='Collections'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative Collections'], name='Cummulative Collections'), secondary_y=True)
fig.update_layout(title_text='Number of Collections Minted per Day')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)
df = Top_5_Collections_Based_on_Mints_Volume  
with c1:
        fig = px.bar(df, x='Contract Address', y='Mint Volume', color='Contract Address', title='Top 5 Collections Based on Mints Volume', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Contract Address', yaxis_title='Volume($LUNA)', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
      
df = Top_5_Collections_Based_on_Mints_Count 
with c2:
        fig = px.bar(df, x='Contract Address', y='Mint Count', color='Contract Address', title='Top 5 Collections Based on Mints Count', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Contract Address', yaxis_title='Mints Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
df = Top_5_Collections_Based_on_Minters_Count
with c1:
        fig = px.bar(df, x='Contract Address', y='Minter Count', color='Contract Address', title='Top 5 Collections Based on Minters Count', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Contract Address', yaxis_title='Minters Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly) 
    

c1, c2, c3 = st.columns(3) 
df = NFT_Mint_Statistics

with c1: 
        fig = px.bar(df, x='Year', y='Average Volume', title='Daily Average Volume of NFT Mints', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$LUNA')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
        fig = px.bar(df, x='Year', y='Median Volume', title='Daily Median Volume of NFT Mints', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$LUNA')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
       
        fig = px.bar(df, x='Year', y='Average NFTs', title='Daily Average Number of NFTs Minted', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='NFTs Count')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
    
        fig = px.bar(df, x='Year', y='Median NFTs', title='Daily Median Number of NFTs Minted', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='NFTs Count')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)      
with c2:  
        fig = px.bar(df, x='Year', y='Average Mint', title='Daily Average Number of TXs Related to Mints', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='TXs Count')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
        fig = px.bar(df, x='Year', y='Median Mint', title='Daily Median Number of TXs Related to Mints', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='TXs Count')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
       
        fig = px.bar(df, x='Year', y='Average Collections', title='Daily Average Number of Collections Minted', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections Count')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
    
        fig = px.bar(df, x='Year', y='Median Collections', title='Daily Median Number of Collections Minted', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections Count')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)       
with c3:  
        fig = px.bar(df, x='Year', y='Average Minters', title='Daily Average Number of Unique Minters', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Minters Count')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
    
        fig = px.bar(df, x='Year', y='Median Minters', title='Daily Median Number of Unique Minters', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Minters Count')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  
  
st.subheader('💵 NFT Sales') 
df = Total_NFT_Sales
c1, c2, c3 = st.columns(3)
    
with c1:
        st.metric(label='**Total Sales Volume:$LUNA (2023)**', value=df['Total Sales Volume'])
        st.metric(label='**Total Sellers Count (2023)**', value=df['Total Sellers Count'].round(2))
with c2:
        st.metric(label='**Total Sales Count (2023)**', value=df['Total Sales Count'])
        st.metric(label='**Total Purchasers Count (2023)**', value=df['Total Purchasers Count'].round(2))
with c3:
        st.metric(label='**Total NFTs Sold Count (2023)**', value=df['Total NFTs Count'])  
        st.metric(label='**Total Collections Count (2023)**', value=df['Total Collections Count'].round(2)) 

df = NFT_Sales 
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['Sales Volume'], name='Sales Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Cummulative Sales Volume'], name='Cummulative Sales Volume'), secondary_y=True)
fig.update_layout(title_text='Sales Volume per Day')
fig.update_yaxes(title_text='$LUNA', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  

fig = px.bar(df, x='Date', y='Sales Count', title='Sales Count per Day')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='TXs Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
     
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['Date'], y=df['NFTs Count'], name='NFTs'), secondary_y=False)
fig.add_trace(go.Line(x=df['Date'], y=df['Collections Count'], name='Collections'), secondary_y=True)
fig.update_layout(title_text='Number of Collections & NFTs Minted per Day')
fig.update_yaxes(title_text='', secondary_y=False)
fig.update_yaxes(title_text='', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = NFT_Users_Count
fig = px.bar(df, x='Date', y='Users Count', color='User Type', title='Number of Unique Sellers & Purchasers', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Users Count', xaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = NFT_Sales_Statistic
c1, c2, c3 = st.columns(3)
    
with c1:
        fig = px.bar(df, x='Year', y='Average Sales Volume', title='Daily Average Sales Volume')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$LUNA')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
        fig = px.bar(df, x='Year', y='Average Purchasers Count', title='Daily Average Purchasers Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Purchasers')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)    
 
with c2:
        fig = px.bar(df, x='Year', y='Average Sales Count', title='Daily Average Sales Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Sales')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='Year', y='Average Collections Count', title='Daily Average Collections Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)    
 
with c3:
        fig = px.bar(df, x='Year', y='Average Sellers Count', title='Daily Average Sellers Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Sellers')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
        fig = px.bar(df, x='Year', y='Average NFTs Count', title='Daily Average NFTs Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='NFTs')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
       
c1, c2, c3 = st.columns(3)
    
with c1:
        fig = px.bar(df, x='Year', y='Median Sales Volume', title='Daily Median Sales Volume')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$LUNA')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
        fig = px.bar(df, x='Year', y='Median Purchasers Count', title='Daily Median Purchasers Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Purchasers')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)    
 
with c2:
        fig = px.bar(df, x='Year', y='Median Sales Count', title='Daily Median Sales Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Sales')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        fig = px.bar(df, x='Year', y='Median Collections Count', title='Daily Median Collections Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Collections')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)    
 
with c3:
        fig = px.bar(df, x='Year', y='Median Sellers Count', title='Daily Median Sellers Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='Sellers')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    
        fig = px.bar(df, x='Year', y='Median NFTs Count', title='Daily Median NFTs Count')
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='NFTs')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)           
       
c1, c2 = st.columns(2)
df = Top_5_Collections_Count_Based_on_Sales_Volume  
with c1:
        fig = px.bar(df, x='Collection', y='Sales Volume', color='Collection', title='Top 5 Collections Based on Sales Volume', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Collection', yaxis_title='$LUNA', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
      
df = Top_5_Collections_Count_Based_on_Sales_Count 
with c2:
        fig = px.bar(df, x='Collection', y='Sales Count', color='Collection', title='Top 5 Collections Based on Sales Count', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Collection', yaxis_title='Sales Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)       
       
c1, c2 = st.columns(2)
df = Top_5_Collections_Count_Based_on_Sellers_Count  
with c1:
        fig = px.bar(df, x='Collection', y='Sellers Count', color='Collection', title='Top 5 Collections Based on Sellers Count', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Collection', yaxis_title='Sellers Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
      
df = Top_5_Collections_Count_Based_on_Purchasers_Count 
with c2:
        fig = px.bar(df, x='Collection', y='Purchaser Count', color='Collection', title='Top 5 Collections Based on Purchasers Count', log_y=False)
        fig.update_layout(showlegend=False, xaxis_title=None, legend_title='Collection', yaxis_title='Purchasers Count', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)       
       
       
