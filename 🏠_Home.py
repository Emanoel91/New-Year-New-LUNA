# Descriptions:
# Help Metrics DAO create the ultimate collection of on-chain analytics, data, and insights with our new Megadashboards challenge! These are serious challenges that 
# require plenty of work — and offer increased payouts in return. Read on for more info:
# We’re putting together the ultimate analytics tool for the NEAR ecosystem, a dazzling dashboard full of glittering insights — and we need your help!
# Create a dashboard that offers a holistic view of the NEAR ecosystem, including activity, supply, staking, and development. Your dashboard should focus on providing 
# everything a newcomer or experienced user should know, organized and presented in a way that is simple to understand, easy to navigate, and understandable and 
#valuable for novices and experienced users alike.


# 📚 Libraries
import streamlit as st
import PIL
from PIL import Image

#near = PIL.Image.open('near_chain_2.png')

# Title
st.set_page_config(page_title='New Year New LUNA', page_icon=':bar_chart:' , layout='wide')
st.title('New Year New LUNA')

# Content
c1, c2 = st.columns(2)

#c1.image(Image.open('Images/near2-logo.png'))

st.subheader('📃 Introduction')


st.write(
    """
1111
    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
2222
    """
)

st.subheader('📖 Guidance')
st.write(
    """
3333
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






