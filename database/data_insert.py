from config import Table, Login
from login import login
import pandas as pd
from datetime import datetime


csv_path = Table.Chapter_path
df = pd.read_csv(csv_path)
# id와 수정 시간 부여
df.loc[:, 'id']=range(1,len(df)+1)
df['id']=df['id'].astype(int)
df['created_at'] = pd.NaT
df.loc[:, 'created_at'] = datetime.now()
conn = login(Login.DB_HOST, Login.DB_USER, Login.DB_PASSWORD, Login.DB_NAME)
cursor = conn.cursor()
columns = "("+", ".join(df.columns)+")"
place_holders = "%s, "*len(df.columns)
place_holders = "("+place_holders.rstrip(', ')+")"

print(df.columns)
cursor.execute("TRUNCATE TABLE chapter")
for index, row in df.iterrows():
    sql = f"""
    INSERT INTO chapter {columns}
    VALUES {place_holders}
    """
    data = tuple([row[column] for column in df.columns])
    cursor.execute(sql, data)
    
conn.commit()
cursor.close()
conn.close()

print("데이터가 잘 입력되었습니다.")