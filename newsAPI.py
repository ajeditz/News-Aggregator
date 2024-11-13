from newsapi import NewsApiClient
from pprint import pprint

# Init
newsapi = NewsApiClient(api_key='90a8858bb01e41628d782ee486433687')



newsapi.get_top_headlines()
# /v2/everything
all_articles = newsapi.get_everything(q='US election',
                                      language='en',
                                      sort_by='relevancy',
                                      qintitle="US election",
                                      page=1,
                                      from_param="2024-10-23",
                                      to="2024-11-06",
                                      sources="CNN, NBC, BBC")

def newsRetriever(query):
    API_response=newsapi.get_everything(q=query,sort_by='relevancy')
    articlesList=API_response['articles']
    newArticlesList=[]
    for article in articlesList:
        title=article['title']
        content=article['content']
        cleaned_article_object={"title":title,"content":content}
        newArticlesList.append(cleaned_article_object)        

    #Taking only first five inputs from the article list
    newArticlesList=newArticlesList[:5]

    return newArticlesList

if __name__=="__main__":
    function_result=newsRetriever(query="Taylor Swift")
    pprint(function_result)


# pprint(all_articles)

