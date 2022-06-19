import pandas as pd
import numpy as np
import  sqlite3

def read_sqlite():
    file_sqlite3 = "./items.db"
    conn = sqlite3.connect(file_sqlite3)
    df = pd.read_sql_query('SELECT * FROM items', conn)
    conn.close()
    return df