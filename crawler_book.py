# 抓取 html
import urllib.request as req
def getData(url):
    # build Request object with Request header info
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    
    # 解析原始碼，取得每篇文章的標題
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser") # 讓 BeattifulSooup 協助我們解析 HTML 格式文件
    titles = root.find_all("span", class_="m_c") # 尋找所有 class"title" 的div標籤
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤（沒有被刪除），印出來
            #print(title.a)
    photo = root.find_all("div", class_="readerPager")
    print(photo.src)   
    # 抓取上一頁的連結
    #nextlink = root.find("a", string= "‹ 上頁") # 找到內文是"‹ 上頁"的a標籤
    #return nextlink["href"]

# 主程序：抓取多個頁面的標題
pageURL = "http://img.chinamaxx.net/n/abroad/hwbook/chinamaxx/11416480/d2f56b50e2b9450aa235102553fb714e/2e0329ddf863bbe09cb8c3b436030588.shtml?tp=jpabroad&fenlei=&t=1&username=twqhdx"

getData(pageURL)
count = 0
'''
while count < 5:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count = count + 1
'''