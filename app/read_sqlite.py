import pandas as pd
import numpy as np
import  sqlite3

def read_sqlite(alphabet):
    file_sqlite3 = "./items.db"
    conn = sqlite3.connect(file_sqlite3)
    df = pd.read_sql_query(f'SELECT DISTINCT * FROM items_{alphabet}', conn)
    conn.close()
    return df