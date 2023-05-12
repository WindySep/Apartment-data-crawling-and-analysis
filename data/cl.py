# 创建人：he
# 开发时间：2023/5/1 20:25
import csv
import pandas as pd
import re


def read(csv_file):
    with open(csv_file, encoding='utf-8') as f:
        r_csv = csv.reader(f)
        headers = next(r_csv)
        # print(headers)
        for row in r_csv:
            print(row)

def clean_up1(csv_file):
    # df = pd.read_csv(csv_file, sep=',')
    # df.dropna(inplace=True)
    # print(df)
    df = pd.read_csv(csv_file, encoding='utf-8')
    df['area'] = df['area'].agg(func=lambda x: x.strip('㎡ '))
    df['price'] = df['price'].agg(func=lambda x: x.strip(' 元/月'))
    df['district'] = df['district'].agg(func=lambda x: x.strip('精选 '))
    df['price'] = df['price'].agg(func=lambda x: x.strip())
    df['area'] = df['area'].agg(func=lambda x: x.strip())
    df['orient'] = df['orient'].agg(func=lambda x: x.strip())
    df['floor'] = df['floor'].agg(func=lambda x: re.sub("\（.*?\）", "", x))
    df['floor'] = df['floor'].agg(func=lambda x: x.strip())
    # 删除指定列
    # df=df.drop(['num'],axis=1)
    df.to_csv(path_or_buf='test4.csv', index=False, encoding='utf-8')




if __name__ == "__main__":
    # for i in range(4):
    #     count = i + 1
    #     csv1 = 'test{}.csv'.format(count)
    #     read(csv1)
    csv_file = 'test5.csv'
    read(csv_file)
    clean_up1(csv_file)