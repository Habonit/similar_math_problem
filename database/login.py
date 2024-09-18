from config import Login
import mysql.connector

def login(host,user,password,database):
    # conn = mysql.connector.connect(
    #     host=Login.DB_HOST,    # MySQL 호스트
    #     user=Login.DB_USER,  # MySQL 사용자 이름
    #     password=Login.DB_PASSWORD,  # MySQL 비밀번호
    #     database=Login.DB_NAME  # 사용할 데이터베이스 이름
    # )
    conn = mysql.connector.connect(
        host=host,    # MySQL 호스트
        user=user,  # MySQL 사용자 이름
        password=password,  # MySQL 비밀번호
        database=database  # 사용할 데이터베이스 이름
    )
    return conn