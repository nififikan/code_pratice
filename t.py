from bs4 import BeautifulSoup
import requests
import xlwt




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

text = ''
for i in range(1, 3):
  url = (f"https://banshi.whlyj.beijing.gov.cn/xyjgptApi/api/creditFile/baseWlml?mainType=lyml&subType=lxsgn&"
         f"name=&page={i}&limit=10&a=d0bb1458-befc-409c-bd8e-15b68ffbe458")
  response = requests.request("GET", url, headers=headers, data=payload)
  text += response.text

print(text)
