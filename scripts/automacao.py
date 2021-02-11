#D:\automacao\drivers\chromedriver_win32
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import testlink


SERVER_URL ="http://45.62.254.148/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
DEVKEY = "d49bd40b3f76b589f5b14a036ed4eba3"

tls = testlink.TestlinkAPIClient(SERVER_URL, DEVKEY)
tls.about()
print(tls.countProjects())


#TCResult = tls.reportTCResult(4,2,"DEMO","p","passou")
#TCResult = tls.reportTCResult(8,2,"DEMO","f","Errado")
#TCResult = tls.reportTCResult(10,2,"DEMO","b","bloqueado")

#driver = webdriver.Chrome('D:/automacao/drivers/chromedriver_win32/chromedriver.exe')

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#Configuracao do driver do chrome
driver = webdriver.Chrome("/usr/local/bin/chromedriver",chrome_options=chrome_options)

                          

#driver.maximize_window()
driver.set_window_size(1920, 1080)
#driver.fullscreen_window()
driver.get('https://www.uol.com.br')
driver.save_screenshot('/opt/suzanoit/automacao/evidencias/evidencia.png')

TCResult = tls.reportTCResult(3,5,"POC","p","Teste executado com sucesso !!")

a_file=open('/opt/suzanoit/automacao/evidencias/evidencia.png', mode='rb')
newAttachment = tls.uploadTestCaseAttachment(a_file, 3, 5,
            title='PNG Example v1', description='PNG Attachment Example for a TestCase v1')


print("Teste executado")
driver.quit()

sys.exit()
