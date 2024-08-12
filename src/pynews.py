from pygooglenews import GoogleNews
import pandas as pd
import constant
import schedule
import time


gn = GoogleNews(lang=constant.lang, country=constant.location)

def news_scrap(cat):
    scrapped_data=gn.search(cat)

    news_data=[]
    for entry in scrapped_data['entries']:
        entry_data={
            'title':entry.title
        }
        news_data.append(entry_data)
    
    # return news_data
    df=pd.DataFrame(news_data)
    print(f"{cat} data scrapped")
    df.to_csv(f'scrapped_news/{cat}.csv', index=False)
    return news_data


# news_cat=['sports','education','technology','business','entertainment','Science','health']

# news_scrap(news_cat)
