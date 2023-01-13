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

st.write(
       """
**A review of all metrics shows that:**
       """
         )    

c1, c2 = st.columns(2)   
with c1:
       st.write(
       """
      ✔ **Metrics that Increased in 2023**
      - Number of active addresses
      - Number of new contracts
      - Number of Liquidity withdrawal
      - Number of liquidity withdrawers
      - Number of collections minted
      - Volume of LUNA delegating
      - Number of delegating
      - Number of redelegating
      - Number of undelegating
      - Number of delegators
      - Number of redelegators
      - Number of Undelegators
      - Number of swaps
      - Number of swappers
      - Volume of LUNA transfers
      - Number of LUNA transfers
      - Number of LUNA senders & Receivers
      - Number of transactions
      - Number of blocks minted
      - Transaction fees
      - Transaction per minute (TPM)
       """
         )
with c2:
         st.write(
         """
        ❌**Metrics that decreased in 2023**
         - Number of new addresses
         - Number of liquidity providing
         - Number of liquidity providers
         - Volume of NFT mints
         - Number of transactions related to NFT mints
         - Number of NFTs minted
         - Volume of redelegating
         - Volume of undelegating
         - Swap volume
         """
          )  
        
st.write(
       """
- **All the above parameters are daily average values.**
- **Since the data is constantly changing, the above report was written on January 11.**
- **While writing this report, the price of LUNA has increased by about 23% compared to the beginning of the year.**
- **Some metrics such as number of transaction per wallet, number of transaction per block and number of unique minters in 2023 have not changed significantly compared to last year.**
       """
         )   
