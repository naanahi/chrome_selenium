import pandas as pd
import numpy as np
import  sqlite3
import settings

def read_sqlite(search_word):
    file_sqlite3 = "./items.db"
    DF_COLUMNS = settings.DF_COLUMNS
    conn = sqlite3.connect(file_sqlite3)
    df = pd.read_sql_query(f'SELECT DISTINCT * FROM items where "{DF_COLUMNS[0]}" LIKE "%{search_word}%"', conn)
    conn.close()
    return df