# 抓取 html
import urllib.request as req
def getData(url):
    # build Request object with Request header info
    request = req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    
    # 解析原始碼，取得每篇文章的標題
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser") # 讓 BeattifulSooup 協助我們解析 HTML 格式文件
    titles = root.find_all("div", class_="title") # 尋找所有 class"title" 的div標籤
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤（沒有被刪除），印出來
            print(title.a.string)
    # 抓取上一頁的連結
    nextlink = root.find("a", string= "‹ 上頁") # 找到內文是"‹ 上頁"的a標籤
    return nextlink["href"]

# 主程序：抓取多個頁面的標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 5:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count = count + 1