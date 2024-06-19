# Updated 20240619 Shanghai Time 14:00

from rich.markdown import Markdown
import warnings
warnings.filterwarnings(action='ignore')
import datetime
from rich.console import Console
import pickle
console = Console(width=90)
import easygui   #https://easygui.readthedocs.io/en/master/api.html

console.print(f'[bold red1]Select the document you want to read...')
file_path = easygui.fileopenbox(filetypes = ["*.dcr","*.lcd","Db search docs files"]) #,"*.pickle"
if file_path:
    console.print(f'[blink2 orange1]Loading...')
    pkl_file = open(file_path, 'rb')
    data_docs = pickle.load(pkl_file)
    pkl_file.close()

    console.print(f'Loaded Document Store - {file_path}')
    console.print(40*'=')
    console.print('\n\n\n')
    """
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
    """ 
    for items in data_docs:
        console.print(f'[bold red1]Title: [red1]{items.metadata["title"]}')
        console.print(f'[bold grey100]Link: [grey100]{items.metadata["source"]}')
        console.print(f'[bold grey100]Authors: [grey100]{items.metadata["author"]}')
        console.print(f'[bold orange1]Snippet: [orange]{items.metadata["snippet"]}')
        console.print(f'[bold orange1]Abstract: [orange1]{items.metadata["summary"]}')
        console.print(f'[bold orange1]MetaImage: [orange1]{items.metadata["meta_img"]}')
        console.print(f'[bold orange1]TOP Image: [orange1]{items.metadata["top_image"]}')
        console.print('---')
        console.print(f'[bold bright_green]Keywords: [bright_green]{items.metadata["keywords"]}')
        console.print('---')
        console.print(f'{items.page_content}')
        console.print(90*'=')

    console.print('\n\n\n')

    console.print(Markdown("> Done"))
else:
    console.print(Markdown("> You didn't choose any file"))    



