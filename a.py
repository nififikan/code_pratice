import pandas as pd
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配`
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import json
import pandas


# 得到指定一个URL的网页内容
def askURL(url):
    payload = {}
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': '_va_ref=%5B%22%22%2C%22%22%2C1699489943%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _va_ses=*; _va_id=f2f859c8f815cbce.1681698590.2.1699490083.1699489943.',
        'Referer': 'https://banshi.whlyj.beijing.gov.cn/xinyong/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'accept': 'application/json',
        'content-type': 'application/json, application/x-www-form-urlencoded',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def get_data():
    data_list = []
    for i in range(1, 376):
        print(f'filter data page {i}')
        url = (f"https://banshi.whlyj.beijing.gov.cn/xyjgptApi/api/creditFile/baseWlml?mainType=lyml&subType=lxsgn&"
               f"name=&page={i}&limit=10&a=d0bb1458-befc-409c-bd8e-15b68ffbe458")
        html = askURL(url)
        tmp_data = json.loads(html)
        data_list += tmp_data['data']['list']

    return data_list


def saveData(datalist, savepath):
    print("save.......")
    col = ("许可证号", "旅行社名称", "联系电话", "地址", "许可证文号", "信用等级")
    excel_pd = pd.DataFrame([])
    for i in range(len(datalist)):
        tmp = datalist[i]
        df_tmp = pd.DataFrame([tmp])
        excel_pd = pd.concat([excel_pd, df_tmp])
    excel_pd.to_excel(savepath, index=False)
    print("ok.......")


if __name__ == '__main__':
    data = get_data()
    file_path = '旅行社信息.xlsx'
    saveData(data, file_path)
