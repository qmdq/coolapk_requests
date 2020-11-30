import requests
import json
import os
#发送一个请求
def save(name,j):
    """负责保存图片的函数
    name=编号
    j=皮肤序号
    """
    name_response = requests.get("https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" + name + "/" + name + "-bigskin-" + str(j) + ".jpg")
    if name_response.status_code == 200:#检查网络是否正常。
        print("正常,开始保存图片%s"%(name+str(j)))
        with open(name+"/"+name+str(j) + ".jpg","wb") as img:#这两行是保存图片的
            img.write(name_response.content)
    else:
        print("请检查网络后重试%s"%name_response.status_code)#网络不正常的提示
        print("\n")

def main(headers):
    #ny = "https://pvp.qq.com/m/m201706/heroList.shtml"
    ny_json = "https://pvp.qq.com/web201605/js/herolist.json"
    response = requests.get(ny_json,headers=headers).text
    html = json.loads(response)
    ny_name = [ ]#创建一个空列表用于储存角色
    with open("hero","w") as t:
        t.write(str(html))
    for hero in html:    
    #遍历json
    #    print(hero)
        hero_name = { }
        #创建存储英雄的列表
        #下列代码将重新命名并添加到hero_name
        hero_name["ename"] = hero["ename"]
        hero_name["name"] = hero["cname"]
        #将处理好的列表添加到列表
        ny_name.append(hero_name)
    
        print(ny_name)
    #def main():
        #Json_get(headers,hero_name)
    for i in ny_name:
        if i in ny_name:
            print(i)
           # print("成功")
            name = str(i["ename"])
            if not os.path.exists(name):
                os.makedirs(name)
            for j in range(1,10):
                if not os.path.exists(name + "/" + name + str(j) + ".jpg"):
                   save(name,j)
                else:
                    continue
if __name__=="__main__":
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        }
    main(headers)  