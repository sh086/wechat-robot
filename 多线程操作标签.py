
from DrissionPage import Chromium
from concurrent.futures import ThreadPoolExecutor

###
# 标签页没有Selenium所谓的焦点的概念 多个标签页可以并行操作
###

# 连接浏览器并获取浏览器对象
browser = Chromium()

# 定义每个线程打开的标签页
def open_url(browser,url):
    tab = browser.new_tab(url)
    print(tab.title)

# 网页列表    
chinese_websites = [
    'https://www.baidu.com',
    'https://www.bilibili.com',
    'https://www.jd.com',
]

# 使用线程池
with ThreadPoolExecutor(max_workers=3) as executor:
    for url in chinese_websites:
        executor.submit(open_url,browser,url)
    executor.shutdown(wait=True)