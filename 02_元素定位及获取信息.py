
from DrissionPage import Chromium

###
# 元素定位
###

# 连接浏览器并获取浏览器对象
browser = Chromium()

###
# 1、普通元素定位
###

# # 获取标签页对象并打开网址
# tab = browser.new_tab('https://www.baidu.com')

# # (1) 通过文本定位
# wenku_button = tab.ele('文库')
# wenku_button.click()

# # (2) 通过属性定位，以id属性为例
# input_box = tab.ele('@id=kw')
# input_box.input('12345')

# # (3) 最精确的定位方法
# search_button = tab.ele('tag:input@@type=submit@@id=su@@value=百度一下')
# search_button.click()
###

###
# 2、iframe定位
###

# # 获取标签页对象并打开网址
# tab = browser.new_tab('https://drissionpage.cn/demos/iframe_diff_domain.html')

# # (1) 最规范写法
# ifram = tab.get_frame('t:iframe')
# ele = ifram.ele('网易首页')
# print(ele)

# # (2) 最简洁 通过将iframe作为元素获取
# iframe = tab.ele('t:iframe')
# ele = iframe('网易首页')
# print(ele)

###

###
# 3、shadow-root定位
###

# # 获取标签页对象并打开网址
# tab = browser.new_tab('https://spiderapi.cn/captcha/turnstile-managed/')

# # shadow-root不能跨级查找 所以要先定位其父元素
# # 但是这里最d顶层的iv没有属性，所以需要先定位到顶层div的兄弟节点p
# bro_p= tab.ele('@id=cf-wait')
# # 然后再通过p节点获取顶层div节点
# top_div = bro_p.after(1)
# print(top_div.html)

# # 获取shadow-root下的iframe元素
# iframe_ele = top_div.sr('t:iframe')
# print(iframe_ele)

###

###
# 4、xpath定位
###

# # 获取标签页对象并打开网址
# tab = browser.new_tab('https://ahrefs.com/backlink-checker/?input=baidu.com&mode=subdomains')
# # 在shadow-root的最顶层div没有任何特征值且无兄弟层元素，所以只能通过xpath定位
# # 在div节点 右击 复制-> 复制完整xpath,并加上 x: 即可
# xpath = 'x://*[@id="root"]/div[1]/section[1]/div/div/div/div/div/div[2]/div[2]/div[2]/form/div[1]/div/div'

# div_ele = tab.ele(xpath)
# print(div_ele)

###

###
# 5、获取元素信息
###
# 获取标签页对象并打开网址
tab = browser.new_tab('https://www.baidu.com')

ai_button = tab.ele('@id=csaitab')

# 获取文本属性
print(ai_button.text)
# # 获取链接属性
print(ai_button.link)
# # 获取指定属性,以class为例
print(ai_button.attr('class'))
# # 获取原生html信息
print(ai_button.html)
# 获取视口坐标 在浏览器的坐标
print(ai_button.rect.viewport_midpoint)
# 获取屏幕坐标 在整个屏幕的坐标
print(ai_button.rect.screen_midpoint)


baidu_logo = tab.ele('@id=s_lg_img')
baidu_logo.save(name = 'baidu_logo')
