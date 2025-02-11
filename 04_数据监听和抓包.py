
from DrissionPage import Chromium
from pprint import pprint

###
# 获取元素信息
###

# 连接浏览器并获取浏览器对象
browser = Chromium()

# 获取最新标签页对象
tab = browser.latest_tab

# 开始监听 指定获取包含该文本的数据包
# 注意 要先开始监听 再打开主页
tab.listen.start('spa1.scrape.center/api/movie')
# 访问主页
tab.get('https://spa1.scrape.center/')

for packet in tab.listen.steps():
    pprint(packet.response.body)