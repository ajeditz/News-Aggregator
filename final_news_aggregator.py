from newsAPI import newsRetriever
from newsSummariser import newsSummariser



def newsAggregator(query:str,) -> str :
    all_articles=newsRetriever(query)
    summary=newsSummariser(all_articles,query)

    return summary



print(newsAggregator("Diwali"))
