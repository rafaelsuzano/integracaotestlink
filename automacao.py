#D:\automacao\drivers\chromedriver_win32

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('D:/automacao/drivers/chromedriver_win32/chromedriver.exe')
#driver = webdriver.Chrome('/opt/suzanoit/automacao/drivers/chrome/chromedriver',0755)


driver.maximize_window()
#driver.fullscreen_window()
driver.get('https://www.uol.com.br')
driver.save_screenshot('evidencia.png')

driver.quit()
