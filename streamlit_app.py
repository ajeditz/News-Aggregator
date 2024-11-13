import streamlit as st
from final_news_aggregator import newsAggregator

st.title("News Aggregator")


biz=st.checkbox("Business")
tech=st.checkbox("Technology")
geo=st.checkbox("Geopolitics")


query=""
if biz:
    query+="Business, "
if tech:
    query+="Technology, "

get_news=st.button("Get news")

st.sidebar.write("this is the sidebar")
# query=st.text_input("Enter the topic on which you want to search about news")

if get_news:
    with st.spinner(text="Collecting the news for you..."):
        summary=newsAggregator(query)

        st.write(f"News Summary is {summary}")