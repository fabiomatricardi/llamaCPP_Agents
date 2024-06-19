
# Updated 20240619 Shanghai Time 14:00

from rich.markdown import Markdown
import warnings
warnings.filterwarnings(action='ignore')
import datetime
from rich.console import Console
from newspaper import Article
import pickle
from langchain.schema.document import Document
console = Console(width=90)


import nltk
nltk.download('punkt')

import os
#from https://python.langchain.com/v0.1/docs/integrations/tools/ddg/
# https://pypi.org/project/duckduckgo-search
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
# https://api.python.langchain.com/en/latest/utilities/langchain_community.utilities.duckduckgo_search.DuckDuckGoSearchAPIWrapper.html
wrapper = DuckDuckGoSearchAPIWrapper(region='us-en', time="y", max_results=10) #time parameter Options: d, w, m, y

console.print(f'[bold red1]What do you want to search?')
research = console.input(f'[bright_green]> ')
console.print(90*'=')
rawdb = wrapper.results(research,max_results=5)

docdocs = []
st = 1
numofdocs = len(rawdb)
for items in rawdb:
    url = items["link"]
    try:  #useful if the url is no reachable
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        kw = []
        #we merge nltk keywords and meta webpage keywords
        for i in article.keywords+article.meta_keywords:
          if i == '': #no blck yeywords for us
            pass
          else:
            kw.append(i)
        if article.text == '': #sometimes there is no text to parse. so we use the snippet
            docdocs.append(Document(page_content = items["snippet"], metadata = {
                'source': items["link"],
                'title': items["title"],
                'snippet': items["snippet"],
                'author':article.authors,
                'keywords':kw,
                'meta_description':article.meta_description,
                'meta_img':article.meta_img,
                'top_image':article.top_image,
                'publish_date':article.publish_date,
                'summary':article.summary}))
        else:
            docdocs.append(Document(page_content = article.text.replace('\n\n',''), metadata = {
                'source': items["link"],
                'title': items["title"],
                'snippet': items["snippet"],
                'author':article.authors,
                'keywords':kw,
                'meta_description':article.meta_description,
                'meta_img':article.meta_img,
                'top_image':article.top_image,
                'publish_date':article.publish_date,
                'summary':article.summary}))
        console.print(f'Prepared Ducment n.{st} out of {numofdocs}')
        st +=1      
    except:
        pass
## SAVE IN PICKLE THE DOCUMENTS SET WITH METADATA
lcdfilename = research.replace(' ','_')+'.lcd'
output = open(lcdfilename, 'wb')
pickle.dump(docdocs, output)
output.close()
console.print(Markdown("> LangChain Documents Data saved..."))
console.print(" - ")


