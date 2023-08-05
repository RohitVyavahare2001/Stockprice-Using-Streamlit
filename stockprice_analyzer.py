import pandas as pd
import streamlit as st
import yfinance as yf
import datetime


st.sidebar.title("Rohit Vyavahare")
st.sidebar.write("""
    Feel free to check out the code on GitHub and connect with me on LinkedIn!
""")

# Links to your Email, LinkedIn, and GitHub
email_link = "rohitvyavahare2001@gmail.com"
linkedin_link = "https://www.linkedin.com/in/rohitvyavahare2001/"
github_link = "https://github.com/RohitVyavahare2001"

# Display links in the sidebar
st.sidebar.markdown(f"📧 [Email]({email_link})")
st.sidebar.markdown(f"🔗 [LinkedIn]({linkedin_link})")
st.sidebar.markdown(f"🐙 [GitHub]({github_link})")


st.write(
    """
    # Stock Price Analyzer

    Shown are the stock prices of Apple
    """
    )

ticker_symbol=st.text_input("Enter stock symbol","AAPL",key="placeholder")


#ticker_symbol="AAPL"

col1,col2=st.columns(2)


#Start date of analysis
with col1:
    start_date=st.date_input("Input starting date",
              datetime.date(2020,1,1))
    
#end date of analysis
with col2:
    end_date=st.date_input("Input Ending date",
              datetime.date(2023,7,31))



ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="1d",start=f"{start_date}",end=f"{end_date}")

st.write(f"""
    ### {ticker_symbol}'sEOD price""")

st.dataframe(ticker_df)


#Showcasing Charts

st.write(""" 
    ## Daily Closing Price Chart
         """)

st.line_chart(ticker_df.Close)

st.write("""
         ## Volume of shares traded each day
         """ )

st.line_chart(ticker_df.Volume)


st.write(
    """
    # © Rohit Vyavahare 
    """
    )
st.markdown (f"🔗 [LinkedIn]({linkedin_link})")           


