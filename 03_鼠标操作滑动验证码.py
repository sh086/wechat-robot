
from DrissionPage import Chromium

###
# 获取元素信息
###

# 连接浏览器并获取浏览器对象
browser = Chromium()

# 获取标签页对象并打开网址
tab = browser.new_tab('http://dun.163.com/trial/sense')

tab.wait(2)
tab.ele('可疑用户-滑动拼图').check()

tab.ele('点击完成验证').check()

# 定位滑块
# move_button_xpath = /html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[2]
move_button_xpath = 'x:/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[2]'
move_button = tab.ele(move_button_xpath)

# 看一下是否正确的定位到滑块了
print(move_button.html)
# 稍等一下 要不然容易提示DrissionPage.errors.NoRectError错误
tab.wait(1)

move_distance_x = 672-526
# actions动作链
# .move_to(move_button) 鼠标移动到滑块上
# .hold(move_button) 按住滑块
# .move(offset_x=move_distance,offset_y=4,duration=2.5) 移动滑块 duration 拖到的持续时间
# .release() 松开滑块
tab.wait(1)
tab.actions.move_to(move_button).hold(move_button).move(offset_x=move_distance_x,offset_y=4,duration=2.5).release()
