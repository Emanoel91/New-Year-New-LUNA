# 📚 Libraries
import streamlit as st
import PIL
from PIL import Image

luna = PIL.Image.open('luna-logo.png')

# Title
st.set_page_config(page_title='New Year New LUNA', page_icon=':bar_chart:' , layout='wide')
st.title('New Year New LUNA')

# Content
c1, c2 = st.columns(2)

c1.image(Image.open('Images/LUNA.png'))

st.subheader('📃 Introduction')


st.write(
    """
After the crash of the **Terra network**, its users and developers made various proposals to restore it. Finally, it was decided that a new network will be launched and 
its cryptocurrencies will be divided among the users of the previous network with a certain ratio. The new network, which started its work on **May 28, 2022**, is called 
**Terra** and its native cryptocurrency is **LUNA**. 

The new **Terra network** is based on the **Cosmos SDK**. The difference between the new network and the previous network is that there is no native **stablecoin** in this 
network and the **Burn/Mint** mechanism has also been removed from it. One of the remarkable points of the new network is that only **10%** of its cryptocurrencies belong to 
its development team and **90%** of the cryptocurrencies are owned by users. Considering this issue, it can be said that the **Terra network** is one of the few blockchain 
networks whose ownership is almost completely in the hands of its user community.
    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
We created a dashboard documenting significant trends in **transactions**, **wallets**, **supply**, **staking**, **development**, or other aspects of the **Terra ecosystem.**

In page '**📱Addresses**', the number of active addresses and new wallets in 2023 is shown. In page '**🛠Development**', users can see the number of new contracts in 2023. 
In page '**💧LP Actions**', all actions, whether providing or withdrawing liquidity in the new year, are monitored. NFTs are considered one of the most attractive ideas 
in the blockchain world. In page '**📸NFTs**', all activities related to minting and buying and selling NFTs using LUNA currency can be seen. All information about the price and 
supply of LUNA can be accessed in page '**💵Price & Supply**'. Staking is when users lock crypto assets for a set period of time to help support the operation of a blockchain. 
All information related to staking of LUNA currency is collected in page '**🩸Staking**'. The data related to the LUNA swap is shown in 
page '**🔄Swap**'. Refer to page '**💸Transfers**' to view the status of LUNA transfers between different addresses. In page '**💳Transactions**', the number of transactions and the amount of fees paid are shown.
    """
)

st.subheader('🔑 Methodology')
st.write(
    """
In this dashboard, [Flipside Crypto](https://flipsidecrypto.xyz/) database is used to extract data related to LUNA currency. All charts show different information from the beginning of 2023 onwards. 
To check the changes of various metrics related to LUNA currency, the average and median of the data in the new year have been compared with the average and median of 
the data in December 2022.
    """
)


c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Analyst: [Emanoel](https://twitter.com/Astiran91)**', icon="📌")
    #c1.image(Image.open('Images/analyst2.JPG'))
with c2:
    st.info('**Database: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="📚")
    #c2.image(Image.open('Images/flipside.JPG'))
with c3:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")
    #c3.image(Image.open('Images/metricsdao.JPG'))






