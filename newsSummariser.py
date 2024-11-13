import google.generativeai as genai
from newsAPI import newsRetriever

import streamlit as st
key=st.secrets["geminiAPIkey"]

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")

query="US elections"
articles=newsRetriever(query=query)


def newsSummariser(articles:list, query ):
    summary=model.generate_content(f"""Given is a list of articles about the topic {query}, each article object has a title and content, 
                                   you need to write a brief in under 400 words from the information given in these articles 
                                   Articles- {articles} """)
    summary=summary.text
    

    
    return summary
    

if __name__=="__main__":
    print(newsSummariser(articles,query))