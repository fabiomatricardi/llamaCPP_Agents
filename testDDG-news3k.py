from tqdm.rich import trange, tqdm
from rich.markdown import Markdown
import warnings
warnings.filterwarnings(action='ignore')
import datetime
from rich.console import Console
from newspaper import Article
import pickle
from langchain.schema.document import Document
console = Console(width=90)

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

"""
for items in rawdb:
    console.print(f'[bold red1]Title: [red1]{items["title"]}')
    console.print(f'[bold orange1]Snippet: [orange1]{items["snippet"]}')
    console.print(f'[bold grey100]Link: [grey100]{items["link"]}')
    console.print(90*'-')
console.print('\n\n\n')
"""


docdocs = []
for items in rawdb:
    url = items["link"]
    try:
        article = Article(url)
        article.download()
        article.parse()
        console.print(f'[bold red1]Title: [red1]{items["title"]}')
        console.print(f'[bold orange1]Snippet: [orange1]{items["snippet"]}')
        console.print(f'[bold grey100]Link: [grey100]{items["link"]}')
        console.print('---')
        if article.text == '':
            console.print('none')
            docdocs.append(Document(page_content = items["snippet"], metadata = {
                'source': items["link"],
                'title': items["title"],
                'snippet': items["snippet"],
                'author':article.authors}))              
        else:
            console.print(article.text)
            docdocs.append(Document(page_content = article.text, metadata = {
                'source': items["link"],
                'title': items["title"],
                'snippet': items["snippet"],
                'author':article.authors}))              
        console.print(90*'-')    
    except:
        pass
## SAVE IN PICKLE THE DOCUMENTS SET WITH METADATA
lcdfilename = research.replace(' ','_')+'.lcd'
output = open(lcdfilename, 'wb')
pickle.dump(docdocs, output)
output.close()
console.print(Markdown("> LangChain Documents Data saved..."))
console.print(" - ")


