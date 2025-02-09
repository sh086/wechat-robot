
from DrissionPage import Chromium

###
# 
###

# 连接浏览器并获取浏览器对象
browser = Chromium()
# 获取标签页对象并打开网址
tab = browser.new_tab('https://www.baidu.com')

# 通过text属性定位
wenku_button = tab.ele('文库')
wenku_button.click()\

https://www.bilibili.com/video/BV19KtVeWEkH?spm_id_from=333.788.player.switch&vd_source=f87f39b1af12eeb6301c7d9944f97ec9