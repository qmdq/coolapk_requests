import requests
import re
import os
from bs4 import BeautifulSoup
import random
url_coolapk = input("请输入要爬取的动态链接:")
response = requests.get(url_coolapk)
#发进get请求。
#print(response.text)
#打印结果
with open("request.txt","w") as p:
    p.write(response.text)
f = re.findall(r'[a-zA-z]+://[^s]*.jpg',response.text)
#使用正则表达式匹配图片地址。
#print("保存图片",f)

for i in f:
#遍历匹配到的图片
   # print("保存图片" + i)
    imgname = i.split("/")[-1]
    #进行图片名称处理
    img = requests.get(i)
  #  print(img.text)
    print("保存图片:" + imgname)
    with open("img/" + imgname,"wb") as file:
    #保存图片
        file.write(img.content)
   # print(i,imgname)
   # print(i)
   # os.system("wget -o" + i)

#f = re.findall('',response.text)
#print("匹配结果",f)
#下半部分为,创建文字标文本,自动保存酷安文本的代码
txt = re.findall(r"来自 \w+ - \w+",response.text)
#匹配文字标题
print(txt)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.findAll("p")[2].text)
text_cooapk = soup.findAll("p")[2].text
file_coolapk = input("请输入文字保存的文本名:")
with open ("txt/" + file_coolapk + ".txt","w") as t:
#获取这篇文章作者的名称。并创建一个相同的txt文件
    t.write(text_cooapk)
