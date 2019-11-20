#D:\automacao\drivers\chromedriver_win32
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#driver = webdriver.Chrome('D:/automacao/drivers/chromedriver_win32/chromedriver.exe')

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')




#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)
                              

#driver.maximize_window()
driver.set_window_size(1920, 1080)
#driver.fullscreen_window()
driver.get('https://www.uol.com.br')
driver.save_screenshot("/opt/suzanoit/automacao/evidencias/evidencia.png")
print("ja foi")
driver.quit()
sys.exit()
