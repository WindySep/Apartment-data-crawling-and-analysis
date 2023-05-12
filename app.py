# 创建人：he
# 开发时间：2023/4/21 12:39

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, make_response
# 导入mysql数据库
import pymysql
# 导入分页的工具类
from pageModel import *
# 向上取整
from math import ceil
import json

def Mysql_db():
    # 建立    Mysql   连接
    conn = pymysql.connect(
        # 本机地址
        host='localhost',
        # 用户名密码
        user='root',
        password='1234',
        # 链接的数据库
        database='lagou',
        # 字符集
        charset='utf8',
    )
    # 获取数据库对象
    return conn

app = Flask(__name__)
'''
flask 基本工作模式
路由解析+模板渲染
app.py配置路由
templates   存放网页模板
'''
app.config['SECRET_KEY'] = '1093595461@qq.com'

# 主页面
@app.route('/')
def index():
    return render_template("index.html")

# 其他页面跳转主页
@app.route('/index')
def home():
    return index()

# 数据库展示清单
@app.route('/showAll')
def showAll():
    # 使用列表保存数据
    dataList = []
    # 打开数据库获取游标
    conn = Mysql_db()
    cursor = conn.cursor()
    #查询数据库中记录的总数量
    tatalRecouds_sql = 'select count(*) from house'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = int(cursor.fetchall()[0][0])
    print("查询数据库中记录的总数量:\n",totalNum)
    # print("当前页面是:\n",pages)
    # 默认进入第一页
    pageindex = 1
    pages = int(pageindex)
    page = pageModel(pages, totalNum)
    # 使用分页类
    if pages > page.totalpage:
        print("这已经是最后一页了!\n最大页面%d\n 你输入的页面%d\n"%(page.totalpage,pages))

    print("----当前页面信息-:::\n最大页面%d\n 从第几个开始:%d\n 当前页面:%d\n 当前页面下标%d\n" % (page.totalpage, page.pagePath, pageindex, page.pages))
    print("最大页面是",page.totalpage)
    # limit 起始位置,每页的长度:
    sqlword = 'select * from house limit %d,%d;'%(page.pagePath,page.pageLong)

    # 引入事务
    try:
        # 执行sql语句
        cursor.execute(sqlword)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 提交
        conn.commit()
        for row in results:
            # 把查找的数据拼接成列表
            dataList.append(row)
    except:
        print("----\n\n\n---- # 异常回滚------执行sql语句时出现错误-----------\n\n\n")
        conn.rollback()

    # print("输出列表:\n\n\n", dataList)
    # 关闭数据库和游标
    cursor.close()
    conn.close()
    return render_template("showAll.html", houses = dataList ,pageindex = pageindex , maxindex = page.totalpage)

# 北京
@app.route('/Beijing')
def Beijing():
    # 使用列表保存数据
    dataList = []
    # 打开数据库获取游标
    conn = Mysql_db()
    cursor = conn.cursor()
    #查询数据库中记录的总数量
    tatalRecouds_sql =  'select count(*) from beijing'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = int(cursor.fetchall()[0][0])
    print("查询数据库中记录的总数量:\n",totalNum)
    # print("当前页面是:\n",pages)
    # 默认进入第一页
    pageindex = 1
    pages = int(pageindex)
    page = pageModel(pages, totalNum)
    # 使用分页类
    if pages > page.totalpage:
        print("这已经是最后一页了!\n最大页面%d\n 你输入的页面%d\n"%(page.totalpage,pages))

    print("----当前页面信息-:::\n最大页面%d\n 从第几个开始:%d\n 当前页面:%d\n 当前页面下标%d\n" % (page.totalpage, page.pagePath, pageindex, page.pages))

    '''
    select * from yourtable limit %d,%d;'%(page.pagePath,page.pageLong)
        起始位置,每页的长度
    select * from yourtable where 查询条件 order by id desc limit 0,10;
        按id倒序排列，且取前10条.
    select * from yourtable where 受条件约束字段 LIKE 文本
        筛选文本.
    '''
    # limit 起始位置,每页的长度:
    sqlword = 'select * from beijing limit %d,%d;'%(page.pagePath,page.pageLong)
    # sqlword_pingfen = 'select * from house order by city desc limit 0,30;'
    # sqlword_pingfen = "select * from yourtable where city like '北京'"

    # 引入事务
    try:
        # 执行sql语句
        cursor.execute(sqlword)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 提交
        conn.commit()
        for row in results:
            # 把查找的数据拼接成列表
            dataList.append(row)
    except:
        print("----\n\n\n---- # 异常回滚------执行sql语句时出现错误-----------\n\n\n")
        conn.rollback()

    # print("输出列表:\n\n\n", dataList)
    # 关闭数据库和游标
    cursor.close()
    conn.close()
    return render_template("Beijing.html", houses = dataList ,pageindex = pageindex , maxindex = page.totalpage)

# 上海
@app.route('/Shanghai')
def Shanghai():
    # 使用列表保存数据
    dataList = []
    # 打开数据库获取游标
    conn = Mysql_db()
    cursor = conn.cursor()
    #查询数据库中记录的总数量
    tatalRecouds_sql =  'select count(*) from shanghai'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = int(cursor.fetchall()[0][0])
    print("查询数据库中记录的总数量:\n",totalNum)
    # print("当前页面是:\n",pages)
    # 默认进入第一页
    pageindex = 1
    pages = int(pageindex)
    page = pageModel(pages, totalNum)
    # 使用分页类
    if pages > page.totalpage:
        print("这已经是最后一页了!\n最大页面%d\n 你输入的页面%d\n"%(page.totalpage,pages))

    print("----当前页面信息-:::\n最大页面%d\n 从第几个开始:%d\n 当前页面:%d\n 当前页面下标%d\n" % (page.totalpage, page.pagePath, pageindex, page.pages))

    '''
    select * from yourtable limit %d,%d;'%(page.pagePath,page.pageLong)
        起始位置,每页的长度
    select * from yourtable where 查询条件 order by id desc limit 0,10;
        按id倒序排列，且取前10条.
    select * from yourtable where 受条件约束字段 LIKE 文本
        筛选文本.
    '''
    # limit 起始位置,每页的长度:
    sqlword = 'select * from shanghai limit %d,%d;'%(page.pagePath,page.pageLong)
    # sqlword_pingfen = 'select * from house order by city desc limit 0,30;'
    # sqlword_pingfen = "select * from yourtable where city like '上海'"

    # 引入事务
    try:
        # 执行sql语句
        cursor.execute(sqlword)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 提交
        conn.commit()
        for row in results:
            # 把查找的数据拼接成列表
            dataList.append(row)
    except:
        print("----\n\n\n---- # 异常回滚------执行sql语句时出现错误-----------\n\n\n")
        conn.rollback()

    # print("输出列表:\n\n\n", dataList)
    # 关闭数据库和游标
    cursor.close()
    conn.close()
    return render_template("Shanghai.html", houses = dataList ,pageindex = pageindex , maxindex = page.totalpage)

# 广州
@app.route('/Guangzhou')
def Guangzhou():
    # 使用列表保存数据
    dataList = []
    # 打开数据库获取游标
    conn = Mysql_db()
    cursor = conn.cursor()
    #查询数据库中记录的总数量
    tatalRecouds_sql =  'select count(*) from guangzhou'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = int(cursor.fetchall()[0][0])
    print("查询数据库中记录的总数量:\n",totalNum)
    # print("当前页面是:\n",pages)
    # 默认进入第一页
    pageindex = 1
    pages = int(pageindex)
    page = pageModel(pages, totalNum)
    # 使用分页类
    if pages > page.totalpage:
        print("这已经是最后一页了!\n最大页面%d\n 你输入的页面%d\n"%(page.totalpage,pages))

    print("----当前页面信息-:::\n最大页面%d\n 从第几个开始:%d\n 当前页面:%d\n 当前页面下标%d\n" % (page.totalpage, page.pagePath, pageindex, page.pages))

    '''
    select * from yourtable limit %d,%d;'%(page.pagePath,page.pageLong)
        起始位置,每页的长度
    select * from yourtable where 查询条件 order by id desc limit 0,10;
        按id倒序排列，且取前10条.
    select * from yourtable where 受条件约束字段 LIKE 文本
        筛选文本.
    '''
    # limit 起始位置,每页的长度:
    sqlword = 'select * from guangzhou limit %d,%d;'%(page.pagePath,page.pageLong)
    # sqlword_pingfen = 'select * from house order by city desc limit 0,30;'
    # sqlword_pingfen = "select * from yourtable where city like '广州'"

    # 引入事务
    try:
        # 执行sql语句
        cursor.execute(sqlword)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 提交
        conn.commit()
        for row in results:
            # 把查找的数据拼接成列表
            dataList.append(row)
    except:
        print("----\n\n\n---- # 异常回滚------执行sql语句时出现错误-----------\n\n\n")
        conn.rollback()

    # print("输出列表:\n\n\n", dataList)
    # 关闭数据库和游标
    cursor.close()
    conn.close()
    return render_template("Guangzhou.html", houses = dataList ,pageindex = pageindex , maxindex = page.totalpage)

# 深圳
@app.route('/Shenzhen')
def Shenzhen():
    # 使用列表保存数据
    dataList = []
    # 打开数据库获取游标
    conn = Mysql_db()
    cursor = conn.cursor()
    #查询数据库中记录的总数量
    tatalRecouds_sql =  'select count(*) from shenzhen'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = int(cursor.fetchall()[0][0])
    print("查询数据库中记录的总数量:\n",totalNum)
    # print("当前页面是:\n",pages)
    # 默认进入第一页
    pageindex = 1
    pages = int(pageindex)
    page = pageModel(pages, totalNum)
    # 使用分页类
    if pages > page.totalpage:
        print("这已经是最后一页了!\n最大页面%d\n 你输入的页面%d\n"%(page.totalpage,pages))

    print("----当前页面信息-:::\n最大页面%d\n 从第几个开始:%d\n 当前页面:%d\n 当前页面下标%d\n" % (page.totalpage, page.pagePath, pageindex, page.pages))

    '''
    select * from yourtable limit %d,%d;'%(page.pagePath,page.pageLong)
        起始位置,每页的长度
    select * from yourtable where 查询条件 order by id desc limit 0,10;
        按id倒序排列，且取前10条.
    select * from yourtable where 受条件约束字段 LIKE 文本
        筛选文本.
    '''
    # limit 起始位置,每页的长度:
    sqlword = 'select * from shenzhen limit %d,%d;'%(page.pagePath,page.pageLong)
    # sqlword_pingfen = 'select * from house order by city desc limit 0,30;'
    # sqlword_pingfen = "select * from yourtable where city like '深圳'"

    # 引入事务
    try:
        # 执行sql语句
        cursor.execute(sqlword)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 提交
        conn.commit()
        for row in results:
            # 把查找的数据拼接成列表
            dataList.append(row)
    except:
        print("----\n\n\n---- # 异常回滚------执行sql语句时出现错误-----------\n\n\n")
        conn.rollback()

    # print("输出列表:\n\n\n", dataList)
    # 关闭数据库和游标
    cursor.close()
    conn.close()
    return render_template("Shenzhen.html", houses = dataList ,pageindex = pageindex , maxindex = page.totalpage)

'''分页和翻页'''
@app.route('/next',methods=['POST'])
def next():
    print("访问next方法")
    # 使用列表保存数据
    dataList = []
    # 打开数据库获取游标
    conn = Mysql_db()
    cursor = conn.cursor()
    # 查询数据库中记录的总数量
    tatalRecouds_sql = 'select count(*) from house'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = int(cursor.fetchall()[0][0])
    print("---pageindex-HTML获取到的数据当前的页面信息是---:", request.get_data())
    # print("当前页面是:\n",pages)\
    # 获取前台当前页信息
    nextpage = int(request.get_data())

    pages = int(nextpage)
    page = pageModel(pages, totalNum)
    # 使用分页类
    if pages > page.totalpage:
        print("这已经是最后一页了!\n最大页面%d\n 你输入的页面%d\n" % (page.totalpage, pages))
    print("计算的下一页是:\n %d"%(nextpage))
    print("----当前页面信息-!\n最大页面 %d \n 从第几个开始: %d \n  当前页号%d\n" % (
    page.totalpage, page.pagePath, page.pages+1))

    # limit 起始位置,每页的长度:
    sqlword = 'select * from house limit %d,%d;' % (page.pagePath, page.pageLong)

    # 引入事务
    try:
        # 执行sql语句
        cursor.execute(sqlword)
        # 获取所有记录列表
        results = cursor.fetchall()
        # 提交
        conn.commit()
        for row in results:
            dataList.append(row)
            # print("\n", row)
    except:
        print("----\n\n\n---执行sql语句时出现错误----\n\n\n")
        # 异常回滚
        conn.rollback()
    # 把新的当前页信息加载到页面
    dataList.append(nextpage)
    # 不测试时注释
    print("输出列表:\n\n\n", dataList)
    # 关闭游标和数据库
    cursor.close()
    conn.close()
    # 返回json数据# 更新下一页的信息
    return json.dumps(dataList)


# 数据分析
# 总体
@app.route('/dataAnalysis')
def dataAnalysis():
    # 设置链表保存数据
    As_dataList = []
    conn = Mysql_db()
    cursor = conn.cursor()
    # 查询数据库中记录的总数量
    tatalRecouds_sql = 'select * from house'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = cursor.fetchall()
    print("数据分析查询数据库中记录的总数量:\n", totalNum)

    # 通过价格分类汇总信息分类汇总
    num0_2 = 0      # 2000以下
    num2_4 = 0      # 2000-4000
    num4_6 = 0      # 4000-6000
    num6_8 = 0      # 6000-8000
    num8_10 = 0     # 8000-10000
    num10_12 = 0    # 10000-12000
    num12_14 = 0    # 12000-14000
    num14 = 0       # 14000以上

    for i in totalNum:
        # 得到要分析的数据---面积---价格
        price = float(i[5])
        # price = float(i[5].replace('"', ''))
        # print("获取名称=%d 面积是= %d \n"%(i[0],area))

        if price <= 2000:
            num0_2 += 1
        elif price > 2000 and price <= 4000:
            num2_4 += 1
        elif price > 4000 and price <= 6000:
            num4_6 += 1
        elif price > 6000 and price <= 8000:
            num6_8 += 1
        elif price > 8000 and price <= 10000:
            num8_10 += 1
        elif price > 10000 and price <= 12000:
            num10_12 += 1
        elif price > 12000 and price <= 14000:
            num12_14 += 1
        else:
            num14 += 1

    # print("num0_20=%d  \n   nnum20_40= %d \n  num40_70=%d \n  num70_100= %d  \n num100=%d\n"%(num0_20,num20_40,num40_70,num70_100,num100))
    # 收集面积的信息,浮点型
    areaAve = 0.0
    area30 = 0
    area30_60 = 0
    area60_80 = 0
    area80_100 = 0
    area100_120 = 0
    area120_140 = 0
    area140 = 0
    allnum = 0
    for j in totalNum:
        # g = float(j[2].replace('"', ''))
        g = float(j[2])

        allnum += 1
        # 计算和
        areaAve = areaAve + float(g)
        if float(g) > 0 and float(g) <= 30:
            area30 += 1
        elif float(g) > 30 and float(g) <= 60:
            area30_60 += 1
        elif float(g) > 60 and float(g) <= 80:
            area60_80 += 1
        elif float(g) > 80 and float(g) <= 100:
            area80_100 += 1
        elif float(g) > 100 and float(g) <= 120:
            area100_120 += 1
        elif float(g) > 120 and float(g) <= 140:
            area120_140 += 1
        elif float(g) > 140:
            area140 += 1

    # 平均数 保留3位小数
    areaAve = round(areaAve / allnum, 3)
    # 把获取到的信息封装成字典
    moneyNum = {"num0_2": num0_2, "num2_4": num2_4, "num4_6": num4_6,
                "num6_8": num6_8,"num8_10": num8_10, "num10_12": num10_12,
                "num12_14": num12_14, "num14": num14}
    areaNum = {"areaAve": areaAve, "area30": area30, "area30_60": area30_60,
                "area60_80": area60_80,"area80_100": area80_100,
                "area100_120": area100_120,"area120_140": area120_140,
               "area140": area140}
    print("输出的列 :moneyNum:", moneyNum)
    print("输出的列 :areaNum:", areaNum)
    print("循环次数", allnum)

    return render_template("dataAnalysis.html", moneyNum=moneyNum, areaNum=areaNum)

# 北京
@app.route('/dataAnalysisB')
def dataAnalysisB():
    # 设置链表保存数据
    As_dataList = []
    conn = Mysql_db()
    cursor = conn.cursor()
    # 查询数据库中记录的总数量
    tatalRecouds_sql = 'select * from beijing'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = cursor.fetchall()
    print("数据分析查询数据库中记录的总数量:\n", totalNum)

    # 通过价格分类汇总信息分类汇总
    num0_2 = 0      # 2000以下
    num2_4 = 0      # 2000-4000
    num4_6 = 0      # 4000-6000
    num6_8 = 0      # 6000-8000
    num8_10 = 0     # 8000-10000
    num10_12 = 0    # 10000-12000
    num12_14 = 0    # 12000-14000
    num14 = 0       # 14000以上

    for i in totalNum:
        # 得到要分析的数据---面积---价格
        price = float(i[5])
        # price = float(i[5].replace('"', ''))
        # print("获取名称=%d 面积是= %d \n"%(i[0],area))

        if price <= 2000:
            num0_2 += 1
        elif price > 2000 and price <= 4000:
            num2_4 += 1
        elif price > 4000 and price <= 6000:
            num4_6 += 1
        elif price > 6000 and price <= 8000:
            num6_8 += 1
        elif price > 8000 and price <= 10000:
            num8_10 += 1
        elif price > 10000 and price <= 12000:
            num10_12 += 1
        elif price > 12000 and price <= 14000:
            num12_14 += 1
        else:
            num14 += 1

    # print("num0_20=%d  \n   nnum20_40= %d \n  num40_70=%d \n  num70_100= %d  \n num100=%d\n"%(num0_20,num20_40,num40_70,num70_100,num100))
    # 收集面积的信息,浮点型
    areaAve = 0.0
    area30 = 0
    area30_60 = 0
    area60_80 = 0
    area80_100 = 0
    area100_120 = 0
    area120_140 = 0
    area140 = 0
    allnum = 0
    for j in totalNum:
        # g = float(j[2].replace('"', ''))
        g = float(j[2])

        allnum += 1
        # 计算和
        areaAve = areaAve + float(g)
        if float(g) > 0 and float(g) <= 30:
            area30 += 1
        elif float(g) > 30 and float(g) <= 60:
            area30_60 += 1
        elif float(g) > 60 and float(g) <= 80:
            area60_80 += 1
        elif float(g) > 80 and float(g) <= 100:
            area80_100 += 1
        elif float(g) > 100 and float(g) <= 120:
            area100_120 += 1
        elif float(g) > 120 and float(g) <= 140:
            area120_140 += 1
        elif float(g) > 140:
            area140 += 1

    # 通过行政区划分类汇总信息分类汇总
    districtDX = 0      # 大兴
    sumPriceDX = 0
    aDX = 0
    districtCP = 0      # 昌平
    sumPriceCP = 0
    aCP = 0
    districtTZ = 0      # 通州
    sumPriceTZ = 0
    aTZ = 0
    districtMTG = 0     # 门头沟
    sumPriceMTG = 0
    aMTG = 0
    districtFT = 0      # 丰台
    sumPriceFT = 0
    aFT = 0
    districtSJS = 0     # 石景山
    sumPriceSJS = 0
    aSJS = 0
    districtCY = 0      # 朝阳
    sumPriceCY = 0
    aCY = 0
    districtHD = 0      # 海淀
    sumPriceHD = 0
    aHD = 0
    districtXC = 0      # 西城
    sumPriceXC = 0
    aXC = 0
    districtDC = 0      # 东城
    sumPriceDC = 0
    aDC = 0
    districtQT = 0      # 其他
    sumPriceQT = 0
    aQT = 0

    for m in totalNum:
        d = m[1]
        p = float(m[5])

        if d == "大兴":
            districtDX += 1
            sumPriceDX += float(m[5])
            aDX += float(m[2])
        elif d == "昌平":
            districtCP += 1
            sumPriceCP += float(m[5])
            aCP += float(m[2])
        elif d == "通州":
            districtTZ += 1
            sumPriceTZ += float(m[5])
            aTZ += float(m[2])
        elif d == "门头沟":
            districtMTG += 1
            sumPriceMTG += float(m[5])
            aMTG += float(m[2])
        elif d == "丰台":
            districtFT += 1
            sumPriceFT += float(m[5])
            aFT += float(m[2])
        elif d == "石景山":
            districtSJS += 1
            sumPriceSJS += float(m[5])
            aSJS += float(m[2])
        elif d == "朝阳":
            districtCY += 1
            sumPriceCY += float(m[5])
            aCY += float(m[2])
        elif d == "海淀":
            districtHD += 1
            sumPriceHD += float(m[5])
            aHD += float(m[2])
        elif d == "西城":
            districtXC += 1
            sumPriceXC += float(m[5])
            aXC += float(m[2])
        elif d == "东城":
            districtDC += 1
            sumPriceDC += float(m[5])
            aDC += float(m[2])
        else:
            districtQT += 1
            sumPriceQT += float(m[5])
            aQT += float(m[2])

    dPriceAveDX = round(sumPriceDX / districtDX, 3)
    dPriceAveCP = round(sumPriceCP / districtCP, 3)
    dPriceAveTZ = round(sumPriceTZ / districtTZ, 3)
    dPriceAveMTG = round(sumPriceMTG / districtMTG, 3)
    dPriceAveFT = round(sumPriceFT / districtFT, 3)
    dPriceAveSJS = round(sumPriceSJS / districtSJS, 3)
    dPriceAveCY = round(sumPriceCY / districtCY, 3)
    dPriceAveHD = round(sumPriceHD / districtHD, 3)
    dPriceAveXC = round(sumPriceXC / districtXC, 3)
    dPriceAveDC = round(sumPriceDC / districtDC, 3)
    dPriceAveQT = round(sumPriceQT / districtQT, 3)

    aveDX = round(sumPriceDX / aDX, 3)
    aveCP = round(sumPriceCP / aCP, 3)
    aveTZ = round(sumPriceTZ / aTZ, 3)
    aveMTG = round(sumPriceMTG / aMTG, 3)
    aveFT = round(sumPriceFT / aFT, 3)
    aveSJS = round(sumPriceSJS / aSJS, 3)
    aveCY = round(sumPriceCY / aCY, 3)
    aveHD = round(sumPriceHD / aHD, 3)
    aveXC = round(sumPriceXC / aXC, 3)
    aveDC = round(sumPriceDC / aDC, 3)
    aveQT = round(sumPriceQT / aQT, 3)

    # 根据楼层位置进行筛选
    floorH = 0      # 高楼层
    fPriveH = 0
    aH = 0
    floorM = 0      # 中楼层
    fPriveM = 0
    aM = 0
    floorL = 0      # 低楼层
    fPriveL = 0
    aL = 0

    for n in totalNum:
        f = n[4]
        p = float(n[5])

        if p < 10000:
            if f == "高楼层":
                floorH += 1
                fPriveH += float(n[5])
                aH += n[2]
            elif f == "中楼层":
                floorM += 1
                fPriveM += float(n[5])
                aM += n[2]
            elif f == "低楼层":
                floorL += 1
                fPriveL += float(n[5])
                aL += n[2]

    fPriveAveH = round(fPriveH / floorH, 3)
    fPriveAveM = round(fPriveM / floorM, 3)
    fPriveAveL = round(fPriveL / floorL, 3)

    aveH = round(fPriveH / aH, 3)
    aveM = round(fPriveM / aM, 3)
    aveL = round(fPriveL / aL, 3)

    # 平均数 保留3位小数
    areaAve = round(areaAve / allnum, 3)
    # 把获取到的信息封装成字典
    moneyNum = {"num0_2": num0_2, "num2_4": num2_4, "num4_6": num4_6,
                "num6_8": num6_8,"num8_10": num8_10, "num10_12": num10_12,
                "num12_14": num12_14, "num14": num14}
    areaNum = {"areaAve": areaAve, "area30": area30, "area30_60": area30_60,
                "area60_80": area60_80,"area80_100": area80_100,
                "area100_120": area100_120,"area120_140": area120_140,
               "area140": area140}
    districtNum = {"districtDX": districtDX, "districtCP": districtCP, "districtTZ": districtTZ,
                   "districtMTG": districtMTG, "districtFT": districtFT, "districtSJS": districtSJS,
                   "districtCY": districtCY, "districtHD": districtHD, "districtXC": districtXC,
                   "districtDC": districtDC, "districtQT": districtQT}
    dPriceAve = {"dPriceAveDX": dPriceAveDX, "dPriceAveCP": dPriceAveCP, "dPriceAveTZ": dPriceAveTZ,
                 "dPriceAveMTG": dPriceAveMTG, "dPriceAveFT": dPriceAveFT, "dPriceAveSJS": dPriceAveSJS,
                 "dPriceAveCY": dPriceAveCY, "dPriceAveHD": dPriceAveHD, "dPriceAveXC": dPriceAveXC,
                 "dPriceAveDC": dPriceAveDC, "dPriceAveQT": dPriceAveQT}
    dAve = {"aveDX": aveDX, "aveCP": aveCP, "aveTZ": aveTZ, "aveMTG": aveMTG,
            "aveFT": aveFT, "aveSJS": aveSJS, "aveCY": aveCY,
            "aveHD": aveHD, "aveXC": aveXC, "aveDC": aveDC, "aveQT": aveQT}
    floorNum = {"floorH": floorH, "floorM": floorM, "floorL": floorM}
    fPriveAve = {"fPriveAveH": fPriveAveH, "fPriveAveM": fPriveAveM, "fPriveAveL": fPriveAveL}
    fAve = {"aveH": aveH, "aveM": aveM, "aveL": aveL}

    print("输出的列 :moneyNum:", moneyNum)
    print("输出的列 :areaNum:", areaNum)
    print("输出的列 :districtNum:", districtNum)
    print("输出的列 :dPriceAve:", dPriceAve)
    print("输出的列 :dAve:", dAve)
    print("输出的列 :floorNum:", floorNum)
    print("输出的列 :fPriveAve:", fPriveAve)
    print("输出的列 :fAve:", fAve)
    print("循环次数", allnum)

    return render_template("dataAnalysisB.html", moneyNum=moneyNum, areaNum=areaNum,
                           districtNum=districtNum, dPriceAve=dPriceAve, dAve=dAve,
                           floorNum=floorNum, fPriveAve=fPriveAve, fAve=fAve)

# 上海
@app.route('/dataAnalysisSH')
def dataAnalysisSH():
    # 设置链表保存数据
    As_dataList = []
    conn = Mysql_db()
    cursor = conn.cursor()
    # 查询数据库中记录的总数量
    tatalRecouds_sql = 'select * from shanghai'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = cursor.fetchall()
    print("数据分析查询数据库中记录的总数量:\n", totalNum)

    # 通过价格分类汇总信息分类汇总
    num0_2 = 0      # 2000以下
    num2_4 = 0      # 2000-4000
    num4_6 = 0      # 4000-6000
    num6_8 = 0      # 6000-8000
    num8_10 = 0     # 8000-10000
    num10_12 = 0    # 10000-12000
    num12_14 = 0    # 12000-14000
    num14 = 0       # 14000以上

    for i in totalNum:
        # 得到要分析的数据---面积---价格
        price = float(i[5])
        # price = float(i[5].replace('"', ''))
        # print("获取名称=%d 面积是= %d \n"%(i[0],area))

        if price <= 2000:
            num0_2 += 1
        elif price > 2000 and price <= 4000:
            num2_4 += 1
        elif price > 4000 and price <= 6000:
            num4_6 += 1
        elif price > 6000 and price <= 8000:
            num6_8 += 1
        elif price > 8000 and price <= 10000:
            num8_10 += 1
        elif price > 10000 and price <= 12000:
            num10_12 += 1
        elif price > 12000 and price <= 14000:
            num12_14 += 1
        else:
            num14 += 1

    # print("num0_20=%d  \n   nnum20_40= %d \n  num40_70=%d \n  num70_100= %d  \n num100=%d\n"%(num0_20,num20_40,num40_70,num70_100,num100))
    # 收集面积的信息,浮点型
    areaAve = 0.0
    area30 = 0
    area30_60 = 0
    area60_80 = 0
    area80_100 = 0
    area100_120 = 0
    area120_140 = 0
    area140 = 0
    allnum = 0
    for j in totalNum:
        # g = float(j[2].replace('"', ''))
        g = float(j[2])

        allnum += 1
        # 计算和
        areaAve = areaAve + float(g)
        if float(g) > 0 and float(g) <= 30:
            area30 += 1
        elif float(g) > 30 and float(g) <= 60:
            area30_60 += 1
        elif float(g) > 60 and float(g) <= 80:
            area60_80 += 1
        elif float(g) > 80 and float(g) <= 100:
            area80_100 += 1
        elif float(g) > 100 and float(g) <= 120:
            area100_120 += 1
        elif float(g) > 120 and float(g) <= 140:
            area120_140 += 1
        elif float(g) > 140:
            area140 += 1

    # 通过行政区划分类汇总信息分类汇总
    districtDX = 0      # 浦东
    sumPriceDX = 0
    aDX = 0
    districtCP = 0      # 黄浦
    sumPriceCP = 0
    aCP = 0
    districtTZ = 0      # 静安
    sumPriceTZ = 0
    aTZ = 0
    districtMTG = 0     # 闵行
    sumPriceMTG = 0
    aMTG = 0
    districtFT = 0      # 嘉定
    sumPriceFT = 0
    aFT = 0
    districtSJS = 0     # 杨浦
    sumPriceSJS = 0
    aSJS = 0
    districtCY = 0      # 徐汇
    sumPriceCY = 0
    aCY = 0
    districtHD = 0      # 长宁
    sumPriceHD = 0
    aHD = 0
    districtXC = 0      # 松江
    sumPriceXC = 0
    aXC = 0
    districtDC = 0      # 宝山
    sumPriceDC = 0
    aDC = 0
    districtQT = 0      # 其他
    sumPriceQT = 0
    aQT = 0

    for m in totalNum:
        d = m[1]
        p = float(m[5])

        if d == "浦东":
            districtDX += 1
            sumPriceDX += float(m[5])
            aDX += float(m[2])
        elif d == "黄浦":
            districtCP += 1
            sumPriceCP += float(m[5])
            aCP += float(m[2])
        elif d == "静安":
            districtTZ += 1
            sumPriceTZ += float(m[5])
            aTZ += float(m[2])
        elif d == "闵行":
            districtMTG += 1
            sumPriceMTG += float(m[5])
            aMTG += float(m[2])
        elif d == "嘉定":
            districtFT += 1
            sumPriceFT += float(m[5])
            aFT += float(m[2])
        elif d == "杨浦":
            districtSJS += 1
            sumPriceSJS += float(m[5])
            aSJS += float(m[2])
        elif d == "徐汇":
            districtCY += 1
            sumPriceCY += float(m[5])
            aCY += float(m[2])
        elif d == "长宁":
            districtHD += 1
            sumPriceHD += float(m[5])
            aHD += float(m[2])
        elif d == "松江":
            districtXC += 1
            sumPriceXC += float(m[5])
            aXC += float(m[2])
        elif d == "宝山":
            districtDC += 1
            sumPriceDC += float(m[5])
            aDC += float(m[2])
        else:
            districtQT += 1
            sumPriceQT += float(m[5])
            aQT += float(m[2])

    dPriceAveDX = round(sumPriceDX / districtDX, 3)
    dPriceAveCP = round(sumPriceCP / districtCP, 3)
    dPriceAveTZ = round(sumPriceTZ / districtTZ, 3)
    dPriceAveMTG = round(sumPriceMTG / districtMTG, 3)
    dPriceAveFT = round(sumPriceFT / districtFT, 3)
    dPriceAveSJS = round(sumPriceSJS / districtSJS, 3)
    dPriceAveCY = round(sumPriceCY / districtCY, 3)
    dPriceAveHD = round(sumPriceHD / districtHD, 3)
    dPriceAveXC = round(sumPriceXC / districtXC, 3)
    dPriceAveDC = round(sumPriceDC / districtDC, 3)
    dPriceAveQT = round(sumPriceQT / districtQT, 3)

    aveDX = round(sumPriceDX / aDX, 3)
    aveCP = round(sumPriceCP / aCP, 3)
    aveTZ = round(sumPriceTZ / aTZ, 3)
    aveMTG = round(sumPriceMTG / aMTG, 3)
    aveFT = round(sumPriceFT / aFT, 3)
    aveSJS = round(sumPriceSJS / aSJS, 3)
    aveCY = round(sumPriceCY / aCY, 3)
    aveHD = round(sumPriceHD / aHD, 3)
    aveXC = round(sumPriceXC / aXC, 3)
    aveDC = round(sumPriceDC / aDC, 3)
    aveQT = round(sumPriceQT / aQT, 3)

    # 根据楼层位置进行筛选
    floorH = 0      # 高楼层
    fPriveH = 0
    aH = 0
    floorM = 0      # 中楼层
    fPriveM = 0
    aM = 0
    floorL = 0      # 低楼层
    fPriveL = 0
    aL = 0

    for n in totalNum:
        f = n[4]
        p = float(n[5])

        if p < 10000:
            if f == "高楼层":
                floorH += 1
                fPriveH += float(n[5])
                aH += n[2]
            elif f == "中楼层":
                floorM += 1
                fPriveM += float(n[5])
                aM += n[2]
            elif f == "低楼层":
                floorL += 1
                fPriveL += float(n[5])
                aL += n[2]

    fPriveAveH = round(fPriveH / floorH, 3)
    fPriveAveM = round(fPriveM / floorM, 3)
    fPriveAveL = round(fPriveL / floorL, 3)

    aveH = round(fPriveH / aH, 3)
    aveM = round(fPriveM / aM, 3)
    aveL = round(fPriveL / aL, 3)

    # 平均数 保留3位小数
    areaAve = round(areaAve / allnum, 3)
    # 把获取到的信息封装成字典
    moneyNum = {"num0_2": num0_2, "num2_4": num2_4, "num4_6": num4_6,
                "num6_8": num6_8,"num8_10": num8_10, "num10_12": num10_12,
                "num12_14": num12_14, "num14": num14}
    areaNum = {"areaAve": areaAve, "area30": area30, "area30_60": area30_60,
                "area60_80": area60_80,"area80_100": area80_100,
                "area100_120": area100_120,"area120_140": area120_140,
               "area140": area140}
    districtNum = {"districtDX": districtDX, "districtCP": districtCP, "districtTZ": districtTZ,
                   "districtMTG": districtMTG, "districtFT": districtFT, "districtSJS": districtSJS,
                   "districtCY": districtCY, "districtHD": districtHD, "districtXC": districtXC,
                   "districtDC": districtDC, "districtQT": districtQT}
    dPriceAve = {"dPriceAveDX": dPriceAveDX, "dPriceAveCP": dPriceAveCP, "dPriceAveTZ": dPriceAveTZ,
                 "dPriceAveMTG": dPriceAveMTG, "dPriceAveFT": dPriceAveFT, "dPriceAveSJS": dPriceAveSJS,
                 "dPriceAveCY": dPriceAveCY, "dPriceAveHD": dPriceAveHD, "dPriceAveXC": dPriceAveXC,
                 "dPriceAveDC": dPriceAveDC, "dPriceAveQT": dPriceAveQT}
    dAve = {"aveDX": aveDX, "aveCP": aveCP, "aveTZ": aveTZ, "aveMTG": aveMTG,
            "aveFT": aveFT, "aveSJS": aveSJS, "aveCY": aveCY,
            "aveHD": aveHD, "aveXC": aveXC, "aveDC": aveDC, "aveQT": aveQT}
    floorNum = {"floorH": floorH, "floorM": floorM, "floorL": floorM}
    fPriveAve = {"fPriveAveH": fPriveAveH, "fPriveAveM": fPriveAveM, "fPriveAveL": fPriveAveL}
    fAve = {"aveH": aveH, "aveM": aveM, "aveL": aveL}

    print("输出的列 :moneyNum:", moneyNum)
    print("输出的列 :areaNum:", areaNum)
    print("输出的列 :districtNum:", districtNum)
    print("输出的列 :dPriceAve:", dPriceAve)
    print("输出的列 :dAve:", dAve)
    print("输出的列 :floorNum:", floorNum)
    print("输出的列 :fPriveAve:", fPriveAve)
    print("输出的列 :fAve:", fAve)
    print("循环次数", allnum)

    return render_template("dataAnalysisSH.html", moneyNum=moneyNum, areaNum=areaNum,
                           districtNum=districtNum, dPriceAve=dPriceAve, dAve=dAve,
                           floorNum=floorNum, fPriveAve=fPriveAve, fAve=fAve)

# 广州
@app.route('/dataAnalysisGZ')
def dataAnalysisGZ():
    # 设置链表保存数据
    As_dataList = []
    conn = Mysql_db()
    cursor = conn.cursor()
    # 查询数据库中记录的总数量
    tatalRecouds_sql = 'select * from guangzhou'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = cursor.fetchall()
    print("数据分析查询数据库中记录的总数量:\n", totalNum)

    # 通过价格分类汇总信息分类汇总
    num0_2 = 0      # 2000以下
    num2_4 = 0      # 2000-4000
    num4_6 = 0      # 4000-6000
    num6_8 = 0      # 6000-8000
    num8_10 = 0     # 8000-10000
    num10_12 = 0    # 10000-12000
    num12_14 = 0    # 12000-14000
    num14 = 0       # 14000以上

    for i in totalNum:
        # 得到要分析的数据---面积---价格
        price = float(i[5])
        # price = float(i[5].replace('"', ''))
        # print("获取名称=%d 面积是= %d \n"%(i[0],area))

        if price <= 2000:
            num0_2 += 1
        elif price > 2000 and price <= 4000:
            num2_4 += 1
        elif price > 4000 and price <= 6000:
            num4_6 += 1
        elif price > 6000 and price <= 8000:
            num6_8 += 1
        elif price > 8000 and price <= 10000:
            num8_10 += 1
        elif price > 10000 and price <= 12000:
            num10_12 += 1
        elif price > 12000 and price <= 14000:
            num12_14 += 1
        else:
            num14 += 1

    # print("num0_20=%d  \n   nnum20_40= %d \n  num40_70=%d \n  num70_100= %d  \n num100=%d\n"%(num0_20,num20_40,num40_70,num70_100,num100))
    # 收集面积的信息,浮点型
    areaAve = 0.0
    area30 = 0
    area30_60 = 0
    area60_80 = 0
    area80_100 = 0
    area100_120 = 0
    area120_140 = 0
    area140 = 0
    allnum = 0
    for j in totalNum:
        # g = float(j[2].replace('"', ''))
        g = float(j[2])

        allnum += 1
        # 计算和
        areaAve = areaAve + float(g)
        if float(g) > 0 and float(g) <= 30:
            area30 += 1
        elif float(g) > 30 and float(g) <= 60:
            area30_60 += 1
        elif float(g) > 60 and float(g) <= 80:
            area60_80 += 1
        elif float(g) > 80 and float(g) <= 100:
            area80_100 += 1
        elif float(g) > 100 and float(g) <= 120:
            area100_120 += 1
        elif float(g) > 120 and float(g) <= 140:
            area120_140 += 1
        elif float(g) > 140:
            area140 += 1

    # 通过行政区划分类汇总信息分类汇总
    districtDX = 0      # 天河
    sumPriceDX = 0
    aDX = 0
    districtCP = 0      # 黄埔
    sumPriceCP = 0
    aCP = 0
    districtTZ = 0      # 越秀
    sumPriceTZ = 0
    aTZ = 0
    districtMTG = 0     # 番禺
    sumPriceMTG = 0
    aMTG = 0
    districtFT = 0      # 海珠
    sumPriceFT = 0
    aFT = 0
    districtSJS = 0     # 白云
    sumPriceSJS = 0
    aSJS = 0
    districtCY = 0      # 南沙
    sumPriceCY = 0
    aCY = 0
    districtHD = 0      # 花都
    sumPriceHD = 0
    aHD = 0
    districtXC = 0      # 增城
    sumPriceXC = 0
    aXC = 0
    districtDC = 0      # 荔湾
    sumPriceDC = 0
    aDC = 0
    districtQT = 0      # 从化
    sumPriceQT = 0
    aQT = 0

    for m in totalNum:
        d = m[1]
        p = float(m[5])

        if d == "天河":
            districtDX += 1
            sumPriceDX += float(m[5])
            aDX += float(m[2])
        elif d == "黄埔":
            districtCP += 1
            sumPriceCP += float(m[5])
            aCP += float(m[2])
        elif d == "越秀":
            districtTZ += 1
            sumPriceTZ += float(m[5])
            aTZ += float(m[2])
        elif d == "番禺":
            districtMTG += 1
            sumPriceMTG += float(m[5])
            aMTG += float(m[2])
        elif d == "海珠":
            districtFT += 1
            sumPriceFT += float(m[5])
            aFT += float(m[2])
        elif d == "白云":
            districtSJS += 1
            sumPriceSJS += float(m[5])
            aSJS += float(m[2])
        elif d == "南沙":
            districtCY += 1
            sumPriceCY += float(m[5])
            aCY += float(m[2])
        elif d == "花都":
            districtHD += 1
            sumPriceHD += float(m[5])
            aHD += float(m[2])
        elif d == "增城":
            districtXC += 1
            sumPriceXC += float(m[5])
            aXC += float(m[2])
        elif d == "荔湾":
            districtDC += 1
            sumPriceDC += float(m[5])
            aDC += float(m[2])
        else:
            districtQT += 1
            sumPriceQT += float(m[5])
            aQT += float(m[2])

    dPriceAveDX = round(sumPriceDX / districtDX, 3)
    dPriceAveCP = round(sumPriceCP / districtCP, 3)
    dPriceAveTZ = round(sumPriceTZ / districtTZ, 3)
    dPriceAveMTG = round(sumPriceMTG / districtMTG, 3)
    dPriceAveFT = round(sumPriceFT / districtFT, 3)
    dPriceAveSJS = round(sumPriceSJS / districtSJS, 3)
    dPriceAveCY = round(sumPriceCY / districtCY, 3)
    dPriceAveHD = round(sumPriceHD / districtHD, 3)
    dPriceAveXC = round(sumPriceXC / districtXC, 3)
    dPriceAveDC = round(sumPriceDC / districtDC, 3)
    dPriceAveQT = round(sumPriceQT / districtQT, 3)

    aveDX = round(sumPriceDX / aDX, 3)
    aveCP = round(sumPriceCP / aCP, 3)
    aveTZ = round(sumPriceTZ / aTZ, 3)
    aveMTG = round(sumPriceMTG / aMTG, 3)
    aveFT = round(sumPriceFT / aFT, 3)
    aveSJS = round(sumPriceSJS / aSJS, 3)
    aveCY = round(sumPriceCY / aCY, 3)
    aveHD = round(sumPriceHD / aHD, 3)
    aveXC = round(sumPriceXC / aXC, 3)
    aveDC = round(sumPriceDC / aDC, 3)
    aveQT = round(sumPriceQT / aQT, 3)

    # 根据楼层位置进行筛选
    floorH = 0      # 高楼层
    fPriveH = 0
    aH = 0
    floorM = 0      # 中楼层
    fPriveM = 0
    aM = 0
    floorL = 0      # 低楼层
    fPriveL = 0
    aL = 0

    for n in totalNum:
        f = n[4]
        p = float(n[5])

        if p < 10000:
            if f == "高楼层":
                floorH += 1
                fPriveH += float(n[5])
                aH += n[2]
            elif f == "中楼层":
                floorM += 1
                fPriveM += float(n[5])
                aM += n[2]
            elif f == "低楼层":
                floorL += 1
                fPriveL += float(n[5])
                aL += n[2]

    fPriveAveH = round(fPriveH / floorH, 3)
    fPriveAveM = round(fPriveM / floorM, 3)
    fPriveAveL = round(fPriveL / floorL, 3)

    aveH = round(fPriveH / aH, 3)
    aveM = round(fPriveM / aM, 3)
    aveL = round(fPriveL / aL, 3)

    # 平均数 保留3位小数
    areaAve = round(areaAve / allnum, 3)
    # 把获取到的信息封装成字典
    moneyNum = {"num0_2": num0_2, "num2_4": num2_4, "num4_6": num4_6,
                "num6_8": num6_8,"num8_10": num8_10, "num10_12": num10_12,
                "num12_14": num12_14, "num14": num14}
    areaNum = {"areaAve": areaAve, "area30": area30, "area30_60": area30_60,
                "area60_80": area60_80,"area80_100": area80_100,
                "area100_120": area100_120,"area120_140": area120_140,
               "area140": area140}
    districtNum = {"districtDX": districtDX, "districtCP": districtCP, "districtTZ": districtTZ,
                   "districtMTG": districtMTG, "districtFT": districtFT, "districtSJS": districtSJS,
                   "districtCY": districtCY, "districtHD": districtHD, "districtXC": districtXC,
                   "districtDC": districtDC, "districtQT": districtQT}
    dPriceAve = {"dPriceAveDX": dPriceAveDX, "dPriceAveCP": dPriceAveCP, "dPriceAveTZ": dPriceAveTZ,
                 "dPriceAveMTG": dPriceAveMTG, "dPriceAveFT": dPriceAveFT, "dPriceAveSJS": dPriceAveSJS,
                 "dPriceAveCY": dPriceAveCY, "dPriceAveHD": dPriceAveHD, "dPriceAveXC": dPriceAveXC,
                 "dPriceAveDC": dPriceAveDC, "dPriceAveQT": dPriceAveQT}
    dAve = {"aveDX": aveDX, "aveCP": aveCP, "aveTZ": aveTZ, "aveMTG": aveMTG,
            "aveFT": aveFT, "aveSJS": aveSJS, "aveCY": aveCY,
            "aveHD": aveHD, "aveXC": aveXC, "aveDC": aveDC, "aveQT": aveQT}
    floorNum = {"floorH": floorH, "floorM": floorM, "floorL": floorM}
    fPriveAve = {"fPriveAveH": fPriveAveH, "fPriveAveM": fPriveAveM, "fPriveAveL": fPriveAveL}
    fAve = {"aveH": aveH, "aveM": aveM, "aveL": aveL}

    print("输出的列 :moneyNum:", moneyNum)
    print("输出的列 :areaNum:", areaNum)
    print("输出的列 :districtNum:", districtNum)
    print("输出的列 :dPriceAve:", dPriceAve)
    print("输出的列 :dAve:", dAve)
    print("输出的列 :floorNum:", floorNum)
    print("输出的列 :fPriveAve:", fPriveAve)
    print("输出的列 :fAve:", fAve)
    print("循环次数", allnum)

    return render_template("dataAnalysisGZ.html", moneyNum=moneyNum, areaNum=areaNum,
                           districtNum=districtNum, dPriceAve=dPriceAve, dAve=dAve,
                           floorNum=floorNum, fPriveAve=fPriveAve, fAve=fAve)

# 深圳
@app.route('/dataAnalysisSZ')
def dataAnalysisSZ():
    # 设置链表保存数据
    As_dataList = []
    conn = Mysql_db()
    cursor = conn.cursor()
    # 查询数据库中记录的总数量
    tatalRecouds_sql = 'select * from shenzhen'
    # 执行sql语句
    cursor.execute(tatalRecouds_sql)
    # 从元组中取出记录条数((数目,),)
    totalNum = cursor.fetchall()
    print("数据分析查询数据库中记录的总数量:\n", totalNum)

    # 通过价格分类汇总信息分类汇总
    num0_2 = 0      # 2000以下
    num2_4 = 0      # 2000-4000
    num4_6 = 0      # 4000-6000
    num6_8 = 0      # 6000-8000
    num8_10 = 0     # 8000-10000
    num10_12 = 0    # 10000-12000
    num12_14 = 0    # 12000-14000
    num14 = 0       # 14000以上

    for i in totalNum:
        # 得到要分析的数据---面积---价格
        price = float(i[5])
        # price = float(i[5].replace('"', ''))
        # print("获取名称=%d 面积是= %d \n"%(i[0],area))

        if price <= 2000:
            num0_2 += 1
        elif price > 2000 and price <= 4000:
            num2_4 += 1
        elif price > 4000 and price <= 6000:
            num4_6 += 1
        elif price > 6000 and price <= 8000:
            num6_8 += 1
        elif price > 8000 and price <= 10000:
            num8_10 += 1
        elif price > 10000 and price <= 12000:
            num10_12 += 1
        elif price > 12000 and price <= 14000:
            num12_14 += 1
        else:
            num14 += 1

    # print("num0_20=%d  \n   nnum20_40= %d \n  num40_70=%d \n  num70_100= %d  \n num100=%d\n"%(num0_20,num20_40,num40_70,num70_100,num100))
    # 收集面积的信息,浮点型
    areaAve = 0.0
    area30 = 0
    area30_60 = 0
    area60_80 = 0
    area80_100 = 0
    area100_120 = 0
    area120_140 = 0
    area140 = 0
    allnum = 0
    for j in totalNum:
        # g = float(j[2].replace('"', ''))
        g = float(j[2])

        allnum += 1
        # 计算和
        areaAve = areaAve + float(g)
        if float(g) > 0 and float(g) <= 30:
            area30 += 1
        elif float(g) > 30 and float(g) <= 60:
            area30_60 += 1
        elif float(g) > 60 and float(g) <= 80:
            area60_80 += 1
        elif float(g) > 80 and float(g) <= 100:
            area80_100 += 1
        elif float(g) > 100 and float(g) <= 120:
            area100_120 += 1
        elif float(g) > 120 and float(g) <= 140:
            area120_140 += 1
        elif float(g) > 140:
            area140 += 1

    # 通过行政区划分类汇总信息分类汇总
    districtDX = 0      # 南山
    sumPriceDX = 0
    aDX = 0
    districtCP = 0      # 福田
    sumPriceCP = 0
    aCP = 0
    districtTZ = 0      # 龙岗
    sumPriceTZ = 0
    aTZ = 0
    districtMTG = 0     # 宝安
    sumPriceMTG = 0
    aMTG = 0
    districtFT = 0      # 龙华
    sumPriceFT = 0
    aFT = 0
    districtSJS = 0     # 罗湖
    sumPriceSJS = 0
    aSJS = 0
    districtCY = 0      # 光明
    sumPriceCY = 0
    aCY = 0
    districtHD = 0      # 坪山
    sumPriceHD = 0
    aHD = 0
    districtXC = 0      # 盐田
    sumPriceXC = 0
    aXC = 0
    districtDC = 0      # 大鹏新区
    sumPriceDC = 0
    aDC = 0


    for m in totalNum:
        d = m[1]
        p = float(m[5])

        if d == "南山区":
            districtDX += 1
            sumPriceDX += float(m[5])
            aDX += float(m[2])
        elif d == "福田区":
            districtCP += 1
            sumPriceCP += float(m[5])
            aCP += float(m[2])
        elif d == "龙岗区":
            districtTZ += 1
            sumPriceTZ += float(m[5])
            aTZ += float(m[2])
        elif d == "宝安区":
            districtMTG += 1
            sumPriceMTG += float(m[5])
            aMTG += float(m[2])
        elif d == "龙华区":
            districtFT += 1
            sumPriceFT += float(m[5])
            aFT += float(m[2])
        elif d == "罗湖区":
            districtSJS += 1
            sumPriceSJS += float(m[5])
            aSJS += float(m[2])
        elif d == "光明区":
            districtCY += 1
            sumPriceCY += float(m[5])
            aCY += float(m[2])
        elif d == "坪山区":
            districtHD += 1
            sumPriceHD += float(m[5])
            aHD += float(m[2])
        elif d == "盐田区":
            districtXC += 1
            sumPriceXC += float(m[5])
            aXC += float(m[2])
        # elif d == "大鹏新区":
        #     districtDC += 1
        #     sumPriceDC += float(m[5])
        #     aDC += float(m[2])


    dPriceAveDX = round(sumPriceDX / districtDX, 3)
    dPriceAveCP = round(sumPriceCP / districtCP, 3)
    dPriceAveTZ = round(sumPriceTZ / districtTZ, 3)
    dPriceAveMTG = round(sumPriceMTG / districtMTG, 3)
    dPriceAveFT = round(sumPriceFT / districtFT, 3)
    dPriceAveSJS = round(sumPriceSJS / districtSJS, 3)
    dPriceAveCY = round(sumPriceCY / districtCY, 3)
    dPriceAveHD = round(sumPriceHD / districtHD, 3)
    dPriceAveXC = round(sumPriceXC / districtXC, 3)
    # dPriceAveDC = round(sumPriceDC / districtDC, 3)

    aveDX = round(sumPriceDX / aDX, 3)
    aveCP = round(sumPriceCP / aCP, 3)
    aveTZ = round(sumPriceTZ / aTZ, 3)
    aveMTG = round(sumPriceMTG / aMTG, 3)
    aveFT = round(sumPriceFT / aFT, 3)
    aveSJS = round(sumPriceSJS / aSJS, 3)
    aveCY = round(sumPriceCY / aCY, 3)
    aveHD = round(sumPriceHD / aHD, 3)
    aveXC = round(sumPriceXC / aXC, 3)
    # aveDC = round(sumPriceDC / aDC, 3)

    # 根据楼层位置进行筛选
    floorH = 0      # 高楼层
    fPriveH = 0
    aH = 0
    floorM = 0      # 中楼层
    fPriveM = 0
    aM = 0
    floorL = 0      # 低楼层
    fPriveL = 0
    aL = 0

    for n in totalNum:
        f = n[4]
        p = float(n[5])

        if p < 10000:
            if f == "高楼层":
                floorH += 1
                fPriveH += float(n[5])
                aH += n[2]
            elif f == "中楼层":
                floorM += 1
                fPriveM += float(n[5])
                aM += n[2]
            elif f == "低楼层":
                floorL += 1
                fPriveL += float(n[5])
                aL += n[2]

    fPriveAveH = round(fPriveH / floorH, 3)
    fPriveAveM = round(fPriveM / floorM, 3)
    fPriveAveL = round(fPriveL / floorL, 3)

    aveH = round(fPriveH / aH, 3)
    aveM = round(fPriveM / aM, 3)
    aveL = round(fPriveL / aL, 3)

    # 平均数 保留3位小数
    areaAve = round(areaAve / allnum, 3)
    # 把获取到的信息封装成字典
    moneyNum = {"num0_2": num0_2, "num2_4": num2_4, "num4_6": num4_6,
                "num6_8": num6_8,"num8_10": num8_10, "num10_12": num10_12,
                "num12_14": num12_14, "num14": num14}
    areaNum = {"areaAve": areaAve, "area30": area30, "area30_60": area30_60,
                "area60_80": area60_80,"area80_100": area80_100,
                "area100_120": area100_120,"area120_140": area120_140,
               "area140": area140}
    districtNum = {"districtDX": districtDX, "districtCP": districtCP, "districtTZ": districtTZ,
                   "districtMTG": districtMTG, "districtFT": districtFT, "districtSJS": districtSJS,
                   "districtCY": districtCY, "districtHD": districtHD, "districtXC": districtXC,
                   "districtDC": districtDC}
    dPriceAve = {"dPriceAveDX": dPriceAveDX, "dPriceAveCP": dPriceAveCP, "dPriceAveTZ": dPriceAveTZ,
                 "dPriceAveMTG": dPriceAveMTG, "dPriceAveFT": dPriceAveFT, "dPriceAveSJS": dPriceAveSJS,
                 "dPriceAveCY": dPriceAveCY, "dPriceAveHD": dPriceAveHD, "dPriceAveXC": dPriceAveXC,
                 # "dPriceAveDC": dPriceAveDC
                 }
    dAve = {"aveDX": aveDX, "aveCP": aveCP, "aveTZ": aveTZ, "aveMTG": aveMTG,
            "aveFT": aveFT, "aveSJS": aveSJS, "aveCY": aveCY,
            "aveHD": aveHD, "aveXC": aveXC,
            # "aveDC": aveDC
            }
    floorNum = {"floorH": floorH, "floorM": floorM, "floorL": floorM}
    fPriveAve = {"fPriveAveH": fPriveAveH, "fPriveAveM": fPriveAveM, "fPriveAveL": fPriveAveL}
    fAve = {"aveH": aveH, "aveM": aveM, "aveL": aveL}

    print("输出的列 :moneyNum:", moneyNum)
    print("输出的列 :areaNum:", areaNum)
    print("输出的列 :districtNum:", districtNum)
    print("输出的列 :dPriceAve:", dPriceAve)
    print("输出的列 :dAve:", dAve)
    print("输出的列 :floorNum:", floorNum)
    print("输出的列 :fPriveAve:", fPriveAve)
    print("输出的列 :fAve:", fAve)

    print("循环次数", allnum)

    return render_template("dataAnalysisSZ.html", moneyNum=moneyNum, areaNum=areaNum,
                           districtNum=districtNum, dPriceAve=dPriceAve, dAve=dAve,
                           floorNum=floorNum, fPriveAve=fPriveAve, fAve=fAve)

# 测试ajax
@app.route('/test')
def textAjax():
    return render_template("test1.html")

# 词云
@app.route('/wordCloud')
def wordCloud():
    return render_template("wordCloud.html")

# 下载模块

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
