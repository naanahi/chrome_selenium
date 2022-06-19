import pandas as pd
import numpy as np
import  sqlite3

def create_sqlite(df):
    file_sqlite3 = "./items.db"
    conn = sqlite3.connect(file_sqlite3)
    df.to_sql('items',conn,if_exists='append',index=None)
    conn.close()