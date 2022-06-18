import time, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import settings
from search_items import search_items
from search_word import search_word

import pandas as pd

URL = settings.URL
ID = settings.ID
PASSWORD = settings.PASSWORD

def main():
    options = webdriver.ChromeOptions()
    ## バックグラウンド実行する際に以下を有効にする
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    ## 遅延処理
    time.sleep(5)

    ## アイテムを検索する
    driver = search_word(driver)
    time.sleep(5)

    ## 現在のURLを取得する
    current_url = driver.current_url

    ## 現在のURLをもとに商品情報(name, price)をリスト化する
    item_info = search_items(current_url)

    df = pd.DataFrame(item_info,columns =['商品名','価格', 'セール価格'])
    df.to_csv("items.csv")

    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()