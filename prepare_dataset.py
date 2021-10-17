from tqdm import tqdm
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup


def get_page(page_url: str):
    page = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(page)

    x = soup.body.find_all('div', attrs={'class': 'fl-post-column'})
    hrefs = [i.find("a")["href"] for i in x]
    page_texts = [get_page_texts(href) for href in tqdm(hrefs)]
    return page_texts


def get_page_texts(page_url: str) -> dict:
    page = urllib.request.urlopen(page_url)
    soup = BeautifulSoup(page)

    x = soup.body.find('div', attrs={'class': 'fl-callout-text'})
    items = x.find_all("p")
    f = []
    for item in items:
        try:
            message = item.text.split("\n")
            author = message[0].split(":")[0]
            text = message[1]
            f.append({"author": author, "text": text})
        except:
            continue
    return f


pages = []
for i in tqdm([1, 2, 3]):
    pages.append(get_page(f"https://www.rev.com/blog/transcript-tag/donald-trump-interview-transcripts/page/{i}"))

flatter = lambda l: [item for subsubitem in l for subitem in subsubitem for item in subitem]

dataset = pd.DataFrame(flatter(pages))

target_author = ["Donald Trump", "President Trump", "President Donald Trump"]
last_context = ""
current_dataset = []
for _, item in dataset.iterrows():
    if item.author in target_author and last_context:
        current_dataset.append({"response": item.text, "context": last_context})
    else:
        last_context = item.text

df = pd.DataFrame(current_dataset)
df.to_csv("donald_trump.csv")
