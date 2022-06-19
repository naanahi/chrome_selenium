from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import settings

def search_word(driver:str) -> str:
    ## 変数初期化
    SEARCH_WORD = settings.SEARCH_WORD
    
    ## ログイン後画面
    search_box = driver.find_element_by_css_selector(".p-header__search input")
    search_box.send_keys(SEARCH_WORD)
    search_button = driver.find_element_by_class_name("p-header__search__submit")
    search_button.send_keys(Keys.ENTER)
    return driver

if __name__ == "__main__":
    pass