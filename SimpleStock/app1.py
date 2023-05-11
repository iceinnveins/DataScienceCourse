import yfinance as yf
import streamlit as st

st.write("""
Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

tickerSymbol = 'GOOGL'

ticketData = yf.Ticker(tickerSymbol)

ticketDf = tickerData.history.(period='id', start='2010-5-31', end='2020,5,31')

st.line_chart(ticketDf.Close)
st.line_chart(ticketDf.Volume)