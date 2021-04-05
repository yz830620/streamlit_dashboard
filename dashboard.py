import streamlit as st
import pandas as pd
import numpy as np
import requests
import tweepy
import config

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

option = st.sidebar.selectbox("Which Dashboard?", ('stockwits', 'wallstreetbets','twitter', 'chart', 'pattern'))

st.header(option)
if option == 'twitter':
    st.subheader("twitter dashboard logic")
    tweets = api.user_timeline('traderstewie')
    st.write(tweets)

if option == "chart":
    st.subheader("this is the chart dashboard")
@st.cache
def check_api():
    return requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")

if option == "stockwits":
    st.subheader("sub")

    symbol = st.sidebar.text_input("Symbol", value="AAPL", max_chars=5)

    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
    data = r.json()
    
    for message in data['messages']:
        st.write(message['body'])
        st.write(message['created_at'])
        st.write(message['user']['username'])
        st.image(message['user']['avatar_url'])