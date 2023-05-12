# -*- codeing = utf-8 -*-
# @Time : 2020/7/1 15:39
# @File : pageModel.py

# 向上取整
from math import ceil

class pageModel:
    def __init__(self,pages,totalNum):
        # 强转为字符串 判断是否越界
        # self 用于初始化得到实例
        try:
            pages = int(pages)
        except:
            pages = 1
        if pages < 1:
            pages = 1

        # 总条目数
        totalNum = totalNum
        # 每页大小
        self.pageLong = 10

        # 当前页面下标 当前页-1
        self.pages = pages-1
        # 总页数  传入页面数量不能比总页面数大
        self.totalpage = ceil(totalNum/self.pageLong)
        # 当前页面地址
        self.pagePath = self.pages*self.pageLong

        # 快速到达首页


        # 最后一页





