import urllib.parse as urlparse
from bs4 import BeautifulSoup
import settings
import time, requests

def search_pages(base_url:str, current_url:str) -> list:
    page_lists = [current_url]
    ## 現在のURLから遷移先を確保する

    html = requests.get(current_url)
    soup = BeautifulSoup(html.content, "html.parser")
    page_list = soup.find(class_="c-pager")
    page_list_children = [text for text in page_list.children]
    for i in page_list_children:
        try:
            links = i.a.get("href")
            
            ## 相対リンクが取得できなかったとき無理やりエラーを発生させる（あまりよろしくない）
            if links == None:
                raise AttributeError
        except AttributeError:
            continue
        url = urlparse.urljoin(base_url, links)
        page_lists.append(url)

    return page_lists

if __name__ == "__main__":
    pass