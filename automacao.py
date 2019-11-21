#D:\automacao\drivers\chromedriver_win32
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import testlink


SERVER_URL ="http://45.62.235.18:2016//testlink/lib/api/xmlrpc/v1/xmlrpc.php"
DEVKEY = "fb9af0eb240ddc1f6b7cbc9c93527cd9"

#driver = webdriver.Chrome('D:/automacao/drivers/chromedriver_win32/chromedriver.exe')

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#Configuração do driver do chrome
driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)

                          

#driver.maximize_window()
driver.set_window_size(1920, 1080)
#driver.fullscreen_window()
driver.get('https://www.uol.com.br')
driver.save_screenshot('opt/suzanoi/evidencias/evidencia.png')

TCResult = tls.reportTCResult(4,4,"DEMO","p","Teste executado com sucesso !!")

a_file=open('opt/suzanoi/evidencias/evidencia.png', mode='rb')
newAttachment = tls.uploadTestCaseAttachment(a_file, 4, 4,
            title='PNG Example v1', description='PNG Attachment Example for a TestCase v1')


print("Teste executado")
driver.quit()

sys.exit()
