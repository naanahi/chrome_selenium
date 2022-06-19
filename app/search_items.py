import time, requests
from timeit import default_timer
from bs4 import BeautifulSoup
import settings
import urllib.parse as urlparse

def search_items(base_url:str, url:str) -> list:
    result = []

    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    item_list = soup.find(class_="item-list")
    ## /* アイテムごとの階層構造を取得する */
    item_list_children = [text for text in item_list.children]
    for str in item_list_children:
        try:
            ## アイテム名を取得する
            name = str.find(class_="item-name")

            ## 商品の詳細ページを取得する
            detail_href = str.find(class_="item-list-image").a.get("href")
            if detail_href != None:
                detail_url = urlparse.urljoin(base_url, detail_href)

            ## 商品画像を取得する
            img = str.find(class_="item-list-image").img.get("src")

            ## 商品価格を取得する
            price = str.find_all(class_="price")

            ## /* 臨時価格が存在するため、1以上とする */
            if 1 <= len(price) <= 2:
                price_list = [i.text for i in price]
            else:
                ## 現在価格が取得できない場合、次の商品情報を処理する
                continue

            if len(price_list) == 1:
                tmp_list = [name.text, price_list[0], None, img, detail_url]
            elif len(price_list) == 2:
                tmp_list = [name.text, price_list[0], price_list[1], img, detail_url]
            else:
                continue
            
            result.append(tmp_list)

            ## 遅延処理
            time.sleep(0.1)

        ## 例外処理
        except TypeError:
            continue
        except AttributeError:
            continue
    ## /* 商品情報のリストを返却する */
    return result

if __name__ == "__main__":
    pass