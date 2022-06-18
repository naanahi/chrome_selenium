import time
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

# # 遅延処理
time.sleep(3)

## ログイン後画面
search_box = driver.find_element_by_css_selector(".p-header__search input")
search_box.send_keys(SEARCH_WORD)
search_button = driver.find_element_by_class_name("p-header__search__submit")
search_button.send_keys(Keys.ENTER)

## 検索後画面
# /* 現在のURLを取得する */
current_url = driver.current_url
html = requests.get(current_url)
soup = BeautifulSoup(html.content, "html.parser")
print(soup.title)

time.sleep(10)
driver.quit()

if __name__ == "__main__":
    pass