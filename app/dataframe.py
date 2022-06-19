import pandas as pd
import numpy as np
import re
import math

def create_dataframe(item_info:list, colnames:list):
    df = pd.DataFrame(item_info,columns =colnames)
    ## 列情報の追加
    df['new-price'] = price_proc(df)
    df['new-sale-price'] = sale_price_proc(df)

    ## str -> int
    df['new-price'] = df['new-price'].astype('int')
    df['new-sale-price'] = df['new-sale-price'].astype('int')

    ## 確定版の価格を算出する
    df['price-commit'] = np.where(df['new-sale-price'] == 0, df['new-price'], df['new-sale-price'])
    ## 割引率を算出する
    df['rate'] = np.where(df['new-sale-price'] == 0, 0, (df['new-sale-price'] / df['new-price']) * 100)
    result_df = df[['item-name', 'price-commit', 'rate', 'detail-url', 'img-url']]
    return result_df

def price_proc(df) -> list:
    pattern = '\w+,?\w+'
    int_price = []
    for i in df['price']:
        search_result = re.search(pattern, i)
        result = search_result.group()
        result = result.replace(',', '')
        int_price.append(result)
    return int_price

def sale_price_proc(df) -> list:
    pattern = '\w+,?\w+'
    int_price_sale = []
    for i in df['sale-price']:
        if i == None:
            result = 0
        else:
            search_result = re.search(pattern, i)
            result = search_result.group()
            result = result.replace(',', '')
        int_price_sale.append(result)
    return int_price_sale

if __name__ == "__main__":
    pass