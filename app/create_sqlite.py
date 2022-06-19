import pandas as pd
import numpy as np
import  sqlite3

def create_sqlite(df, alphabet):
    file_sqlite3 = "./items.db"
    conn = sqlite3.connect(file_sqlite3)
    ## 検索したワード（ローマ字）でテーブルを作成する）
    df.to_sql(f'items_{alphabet}' ,conn,if_exists='append',index=None)
    conn.close()