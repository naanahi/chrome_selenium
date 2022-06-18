import time, requests
from bs4 import BeautifulSoup
import settings

def search_items(url:str) -> list:
    result = []

    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    item_list = soup.find(class_="item-list")
    ## /* アイテムごとの階層構造を取得する */
    item_list_children = [text for text in item_list.children]
    for str in item_list_children:
        try:
            ## /* アイテム名と価格を取得する */
            name = str.find(class_="item-name")
            price = str.find_all(class_="price")

            ## /* 臨時価格が存在するため、1以上とする */
            if len(price) >= 1:
                price_list = [i.text for i in price]
            else:
                ## 現在価格が取得できない場合、次の商品情報を処理する
                continue

            item_dict = {"name" : name.text, "price": price_list}
            result.append(item_dict)

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