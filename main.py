from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep, time
from random import choice
from decimal import Decimal
from json import load, dump
from os.path import exists
from sys import exit

def check_or_creat_setting_file():
    if not exists("./setting.json"):
        default = {
            "sheet_url": "https://docs.qq.com/sheet/DREVLcHpPc0Z2dEZU",
            "driver_path": "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe",
            "user_name": "Name",
            "temp_set": {
                "max": "37.0",
                "min": "36.4",
                "step": "0.01"
            },
            "login_wait": 3,
            "wait_max": 15,
            "keyboard_wait": 0.5,
            "fill_once": 3,
            "save_wait": 3,
            "is_headless": True
        }
        dump(default, open("./setting.json", "w", encoding='utf-8'))
        print("未检测到配置文件")
        print("已自动按照默认设置生成了配置文件，请参照README.md中的说明自行更改后再次启动本程序")
        print("按ENTER键关闭...")
        input()
        exit(0)
def load_setting():
    return load(open("./setting.json", "r", encoding='utf-8'))
def float_range(min, max, step):
    i = Decimal(min)
    list = []
    while i <= Decimal(max):
        list.append(i)
        i += Decimal(step)
    return list
# 加载表格窗口
def load_window(driver_path, sheet_url, head_less):
    global setting
    chrome_options = Options()
    chrome_options.add_argument('log-level=3') 
    chrome_options.add_argument('--incognito')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if head_less:
        chrome_options.add_argument("--headless") 
    else:
        chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
    browser.implicitly_wait(15)
    
    browser.get(sheet_url)
    return browser
# 方式为点击QQ图标自动登录
def login(browser):
    browser.find_element(By.ID, 'header-login-btn').click()
    browser.find_element(By.XPATH, '//*[@id="docs-component-login-container"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[2]').click()
    browser.switch_to.frame("login_frame")
    browser.find_element(By.XPATH, '//*[@id="qlogin_list"]/a').click()
    browser.switch_to.default_content()
def find_pos(browser, user_name, keyboard_wait):
    # 聚焦到表格
    browser.find_element(By.XPATH, '//*[@id="canvasContainer"]/div[1]/div[2]').click()
    sleep(keyboard_wait)
    # 返回左上角
    browser.find_element(By.XPATH, '//*[@id="canvasContainer"]/div[1]/div[2]').send_keys(Keys.CONTROL, Keys.HOME)
    # 向右寻找用户列
    while browser.find_element(By.ID, 'alloy-simple-text-editor').text != user_name:
        browser.find_element(By.XPATH, '//*[@id="canvasContainer"]/div[1]/div[2]').send_keys(Keys.TAB)
        sleep(keyboard_wait)
    # 向下寻找未被填写位置
    while browser.find_element(By.ID, 'alloy-simple-text-editor').text != "":
        browser.find_element(By.XPATH, '//*[@id="canvasContainer"]/div[1]/div[2]').send_keys(Keys.ENTER)
        sleep(keyboard_wait)
def fill_sheet(browser, fill_once, temp_list, keyboard_wait):
    for i in range(fill_once):
        browser.find_element(By.ID, 'alloy-rich-text-editor').send_keys(str(choice(temp_list)))
        sleep(keyboard_wait)
        browser.find_element(By.ID, 'alloy-rich-text-editor').send_keys(Keys.ENTER)
        sleep(keyboard_wait)



if __name__ == '__main__':
    start_time = time()
    check_or_creat_setting_file()
    setting = load_setting()
    # 初始化浏览器窗口
    browser = load_window(setting["driver_path"], setting["sheet_url"], setting["is_headless"])
    print("浏览器窗口创建成功")
    # 自动登录
    login(browser)
    print("登录成功")
    sleep(setting["login_wait"])
    # 调整位置
    find_pos(browser, setting["user_name"], setting["keyboard_wait"])
    print("已定位起始位置")
    # 输出温度
    fill_sheet(browser, setting["fill_once"], float_range(setting["temp_set"]["min"], setting["temp_set"]["max"], setting["temp_set"]["step"]), setting["keyboard_wait"])
    print("温度填写完毕")
    sleep(setting["save_wait"])
    browser.close()
    print("任务完成，总耗时"+str(int(time()-start_time))+"秒")
    print("按ENTER键关闭...")
    input()
    exit(0)
        