# 创建人：he
# 开发时间：2023/5/1 22:08
# 导入pymysql方法
import pandas as pd
import pymysql
import csv
from collections import namedtuple

def get_data(file_name):
    with open(file_name, encoding='utf-8') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        # print(headers)
        Row = namedtuple('Row', headers)
        for r in f_csv:
            yield Row(*r)

def execute_sql(conn, sql):
    with conn.cursor() as cur:
        cur.execute(sql)
        print('执行成功')

def main():
    conn = pymysql.connect(
        # 本机地址
        host='localhost',
        # 用户名密码
        user='root',
        password='1234',
        # 链接的数据库
        database='lagou',
        port = 3306,
    # 字符集
        charset='utf8',)

# 将CSV文件中的数据插入MySQL数据表中
    SQL_FORMAT = """insert into shenzhen values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')"""
    conn.autocommit(1)
    for t in get_data('test1.csv'):
        print(t.title, t.district, t.area, t.orient, t.floor, t.price, t.city)
        sql = SQL_FORMAT.format(t.title, t.district, t.area, t.orient, t.floor, t.price, t.city)
        print(sql)
        execute_sql(conn, sql)
    conn.commit()  # 提交到数据库
    conn.close()  # 关闭数据库服务

if __name__ == '__main__':
    main()

