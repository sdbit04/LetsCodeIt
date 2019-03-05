from selenium import webdriver
import os
import time
def take_screen_shot(message):
    Driver = webdriver.Chrome(executable_path=r"C:\BrowserDriver\chromedriver.exe")
    # decide directory location
    rela_screen_shot_dir = "..\\ScreenShots"
    module_directory2 = os.path.dirname(__file__)
    realpath = os.path.realpath(os.path.join(module_directory2, rela_screen_shot_dir))
    # decide file name
    filename = message + str(time.time())
    full_path = realpath + '\\' + filename + '.png'
    # save screen_shot with the file name
    print(full_path)
    Driver.get("https://www.google.com")
    Driver.save_screenshot(full_path)
    time.sleep(5)
    Driver.close()

take_screen_shot("swapan")
