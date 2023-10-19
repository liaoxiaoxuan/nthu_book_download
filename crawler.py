# 抓取 html
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
# build Request object with Request header info
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

# 解析原始碼，取得每篇文章的標題
import bs4
root = bs4.BeautifulSoup(data, "html.parser") # 讓 BeattifulSooup 協助我們解析 HTML 格式文件
titles = root.find_all("div", class_="title") # 尋找所有 class"title" 的div標籤
for title in titles:
    if title.a != None: #如果標題包含 a 標籤（沒有被刪除），印出來
        print(title.a.string)

