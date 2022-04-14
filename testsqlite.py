from flask import Flask,render_template
import sqlite3
from flask import request,redirect,url_for
import time
import random
import string



countryUnio = ['德国', '意大利', '英国', '西班牙', '韩国', '印度', '新西兰', '黎巴嫩', '中国香港', '墨西哥', '巴西', '爱尔兰', '阿根廷', '丹麦', '泰国', '中国大陆', '美国', '伊朗', '澳大利亚', '瑞典', '日本', '法国', '中国台湾', '加拿大']
movies = []
conn = sqlite3.connect("imdbmovie.db")
cur = conn.cursor()
sql = "select * from movie250 "
data = cur.execute(sql)
for item in data:
    data = []
    for item2 in item:
        data.append(item2)
    movies.append(data)
cur.close()
conn.close()


def delRecommov(*args):  #*args代表一个元组
    myCountrys = []
    myTypes = []  # 传入选择的电影类型信息
    myYears = []  # 存放传入的年代数据

    for mov in args[0]:
        myCountrys.append(movies[mov-1][11])
        myCountrys = list(set(myCountrys))  # 去除重复

        firstType = movies[mov-1][12].split('|')
        for item in firstType:
            myTypes.append(item)
        myTypes = list(set(myTypes)) #去除重复

        myYears.append(movies[mov-1][10])
        myYears = list(set(myYears))  # 去除重复

        # 根据国家选出电影
    countryChoosed = []
    print(myCountrys)
    for myCountry in myCountrys:
        for movie in movies:
            if movie[11] == myCountry:
                countryChoosed.append(movie[0])  #得到的是电影序号
    print(sorted(countryChoosed))
    print(len(countryChoosed))

    # 通过电影类型进行筛选


    myTypes.append('剧情')
    myTypes.append('科幻')
    myTypes.append('惊悚片')
    print(myTypes)

    typeChoosed = []  # 存储剧情筛选后的电影编号

    # 给每个电影末端加上权重位 初始值为0
    for countryChooseNum in countryChoosed:
        movies[countryChooseNum-1].append(0)
        # print(movies[countryChooseNum])

    for countryChooseNum in countryChoosed:
        for myType in myTypes:
            # 对原始的电影类型进行处理--拆开多个剧情
            types = movies[countryChooseNum-1][12].split('|')
            for solotype in types:
                if solotype == myType:
                    movies[countryChooseNum-1][13] = movies[countryChooseNum-1][13] + 1  # 赋权
        # 如果电影的权值不为0 将电影选中
        if movies[countryChooseNum-1][13] != 0:
            typeChoosed.append(movies[countryChooseNum-1][0])
    print(sorted(typeChoosed))
    print(len(typeChoosed))

    # 通过电影年代进行筛选 首先对电影年代进行分类


    yearChoosed = []

    for typeChoosedNum in typeChoosed:
        for myyear in myYears:
            if movies[typeChoosedNum - 1][10] <= myyear + 2 and myYears[1] - 2 < movies[typeChoosedNum - 1][10]:
                yearChoosed.append(movies[typeChoosedNum - 1][0])
    yearChoosed = list(set(yearChoosed))
    print(sorted(yearChoosed))
    print(len(yearChoosed))

    finalChoosed =  sorted(yearChoosed)


if __name__ == '__main__':
    data = [120,78,13]
    delRecommov(data)

