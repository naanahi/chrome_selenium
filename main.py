from re import I
import time
from psutil import cpu_times
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import settings
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()

## バックグラウンド実行する際に以下を有効にする
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

URL = settings.URL
ID = settings.ID
PASSWORD = settings.PASSWORD
SEARCH_WORD = settings.SEARCH_WORD

## 初期画面からログイン画面に遷移する
driver.get(URL)

# login = driver.find_element_by_xpath("/html/body/header/div/div/ul/li[3]/a")
# login.click()

# # 遅延処理
# time.sleep(3)

# ## IDとパスワードを入力する
# user = driver.find_element_by_name("id")
# user.send_keys(ID)
# password = driver.find_element_by_name("passwd")
# password.send_keys(PASSWORD)
# button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/form/div/input")
# button.send_keys(Keys.ENTER)

## 遅延処理
time.sleep(5)

## ログイン後画面
search_box = driver.find_element_by_css_selector(".p-header__search input")
search_box.send_keys(SEARCH_WORD)
search_button = driver.find_element_by_class_name("p-header__search__submit")
search_button.send_keys(Keys.ENTER)

## 検索後画面
# /* 現在のURLを取得する */
time.sleep(5)
current_url = driver.current_url

html = requests.get(current_url)
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

        print(name.text)
        print(price_list)

        ## 遅延処理
        time.sleep(0.1)

    ## 例外処理
    except TypeError:
        continue
    except AttributeError:
        continue

time.sleep(10)
driver.quit()

if __name__ == "__main__":
    pass