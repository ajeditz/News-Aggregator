import streamlit as st
from final_news_aggregator import newsAggregator

# Center align the title
st.markdown("<h1 style='text-align: center;'>News Aggregator</h1>", unsafe_allow_html=True)



# Sidebar with instructions and app functionality details
st.sidebar.write("### Instructions")
st.sidebar.write("Select the topics you want to include in the news summary.")
st.sidebar.write("Then click on the 'Get News' button to generate a summarized report.")
st.sidebar.write("---")
st.sidebar.write("### How It Works")
st.sidebar.write("This app uses **newsAPI** to fetch the latest news and **Gemini** to summarize the results.")

# Columns for topic selection and news summary
col1, col2 = st.columns([1, 2])  # Adjusted width ratio for larger summary column

# Button to get news
with col1:
    # Instruction for topic selection
    st.write("Select the topics you are interested in to receive a summarized news report.")
    
    # Topics checkboxes
    biz = st.checkbox("Business")
    tech = st.checkbox("Technology")
    geo = st.checkbox("Geopolitics")
    celebrity = st.checkbox("Celebrity Gossip")
    sports = st.checkbox("Sports")
    health = st.checkbox("Health")

    query = ""
    if biz:
        query += "Business, "
    if tech:
        query += "Technology, "
    if geo:
        query += "Geopolitics, "
    if celebrity:
        query += "Celebrity Gossip, "
    if sports:
        query += "Sports, "
    if health:
        query += "Health, "

    get_news = st.button("Get News")

with col2:
    st.write("### News Summary")

# Display news summary in the second column
if get_news:
    with st.spinner(text="Collecting the news for you..."):
        summary = newsAggregator(query)
        with col2:
            
            st.write(value=f"{summary}")
