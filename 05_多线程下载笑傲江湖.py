from DrissionPage import Chromium, ChromiumOptions
from pprint import pprint
import threading
import concurrent.futures

# 设置Chromium浏览器选项，使用系统用户路径
# 注意 使用use_system_user_path() 必须关闭已打开的谷歌浏览器
co = ChromiumOptions().use_system_user_path()

# 连接浏览器并获取浏览器对象
browser = Chromium(co)

# 获取标签页对象并打开目标网址
tab_instance = browser.new_tab('https://www.jinyongwang.net/xiao/')

chapter_dict = {}
# # XPath定位到章节列表的无序列表
chapters_xpath = 'x://*[@id="pu_box"]/div[3]/ul'
# 从网页中提取章节标题和链接
for chapter in tab_instance(chapters_xpath).eles('t:a'):
    chapter_dict[chapter.text] = chapter.link

# # # 打印提取到的章节字典
pprint(chapter_dict)
list_chapter = list(chapter_dict.keys())

def fetch_and_save_chapter(chapter_title, chapter_url):
    
    new_tab = browser.new_tab(chapter_url)  # 打开章节链接
    chapter_content = new_tab('@id=box').text  # 获取章节内容
    print(chapter_content)

    print(f"正在下载笑傲江湖 {chapter_title}")
    tab_instance.wait(1)
    
    # 将章节内容写入文件
    with open(f'./笑傲江湖_{chapter_title}.txt', 'w', encoding='utf-8') as file:
        file.write(chapter_content)
       
    #threading.Thread(target=new_tab.close).start()  # 关闭新标签页
    new_tab.close()
    
# - 单线程
# for aa in list_chapter:
#     fetch_and_save_chapter(aa, chapter_dict[aa])

#- 多线程
def main():
    # 创建一个线程池，最多允许 4 个线程同时运行
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # 提交多个任务到线程池
        futures = [executor.submit(fetch_and_save_chapter, chapter_title, chapter_url) 
                   for chapter_title, chapter_url in chapter_dict.items()]

if __name__ == "__main__":
    main()
    input("按下回车键退出")