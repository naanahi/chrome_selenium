import time, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import settings
from search_items import search_items
from search_word import search_word
from search_pages import search_pages
import pandas as pd
import urllib.parse as urlparse



def main():
    ## 変数初期化
    URL = settings.URL
    SEARCH_WORD = settings.SEARCH_WORD
    DF_COLUMNS = settings.DF_COLUMNS

    ## ドライバオプションの指定？
    options = webdriver.ChromeOptions()
    ## バックグラウンド実行する際に以下を有効にする
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    time.sleep(5)

    ## アイテムを検索する
    driver = search_word(driver)
    time.sleep(5)

    ## 現在のURLから、遷移先ページを取得する（ページネーションが存在する場合、要素が複数になる）
    search_page_list = search_pages(URL, driver.current_url)

    for index, search_page in enumerate(search_page_list):
        # 遷移先ページURLをもとに商品情報(name, price)をリスト化する
        item_info = search_items(URL, search_page)

        # データフレームを作成する
        df = pd.DataFrame(item_info,columns =DF_COLUMNS)

        # データフレームをCSV出力する
        df.to_csv(f".\\csvdata\\Search_{SEARCH_WORD}_No.{index}.csv")
        time.sleep(5)

        return df

    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()