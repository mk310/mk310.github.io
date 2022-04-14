# -*- coding = utf-8 -*-
# @Time: 2022/4/8 19:25
# @Author: mk310
# @File: testflask.py
# @Software:PyCharm
from flask import Flask,render_template
import sqlite3
from flask import request,redirect,url_for
import time
import random

app = Flask(__name__)



# @app.route('/')
# def index():  # put application's code here
#     return render_template("index.html")  #默认指向templates

#得到电影数据
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






# 随机数组
randomNums = []
while 1:
    i = random.randint(0, 250)
    randomNums.append(i)
    if len(set(randomNums)) == 6:
        break

randomMovs = []  # 存储随机生成的电影
for i in randomNums:
    randomMovs.append(movies[i - 1])
choose = []

@app.route('/',methods = ['GET','POST'])
def recommov():

    if request.method == 'GET': #无表格提交

        return render_template("recommov.html",randomMovs =randomMovs,choose = choose)
    else:
        #有表格提交
        #删除上次提交的数据
        while len(choose) != 0:
            choose.pop()
        #读取数据
        text = request.form.get('mov0')
        if text != None:
            choose.append(text)
        text = request.form.get('mov1')
        if text != None:
            choose.append(text)
        text = request.form.get('mov2')
        if text != None:
            choose.append(text)
        text = request.form.get('mov3')
        if text != None:
            choose.append(text)
        text = request.form.get('mov4')
        if text != None:
            choose.append(text)
        text = request.form.get('mov5')
        if text != None:
            choose.append(text)

        return redirect(url_for('recommov'))





if __name__ == '__main__':
    app.run()
