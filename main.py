import time, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import settings, search_items, search_word

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
    driver = search_word.search_word(driver)
    time.sleep(5)

    ## 現在のURLを取得する
    current_url = driver.current_url

    ## 現在のURLをもとに商品情報(name, price)をリスト化する
    item_info = search_items.search_items(current_url)
    print(item_info)

    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()