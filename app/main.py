import time, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import settings
from search_items import search_items
from search_word import search_word
from search_pages import search_pages
from dataframe import create_dataframe
from create_sqlite import create_sqlite
from read_sqlite import read_sqlite
from change_word import change_word

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
    ## Dockerで動かすとなぜか怒られるので以下を追加
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    time.sleep(5)

    ## アイテムを検索する
    driver = search_word(driver)
    time.sleep(5)

    ## 検索に使用したワードをローマ字に変換しておく
    search_roman_alphabet = change_word(SEARCH_WORD)

    ## 現在のURLから、遷移先ページを取得する（ページネーションが存在する場合、要素が複数になる）
    search_page_list = search_pages(URL, driver.current_url)

    for index, search_page in enumerate(search_page_list):
        # 遷移先ページURLをもとに商品情報(name, price)をリスト化する
        item_info = search_items(URL, search_page)

        # データフレームを作成する
        df = create_dataframe(item_info, DF_COLUMNS)

        # データフレームをDBに登録する
        create_sqlite(df, search_roman_alphabet)

        # DBの読み出し(条件指定を行いたい)
        df = read_sqlite(search_roman_alphabet)

        # データフレームをCSV出力する
        df.to_csv(f"result_{search_roman_alphabet}.csv", index=False)

        time.sleep(5)

    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()