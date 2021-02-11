#D:\automacao\drivers\chromedriver_win32
import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import testlink


SERVER_URL ="http://142.47.217.91/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
DEVKEY = "73dd23a931a012880ca6735aefcac8ac"

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

driver =  webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options) 

                          

#driver.maximize_window()
driver.set_window_size(1920, 1080)
#driver.fullscreen_window()
driver.get('https://www.uol.com.br')
driver.save_screenshot('/opt/suzanoit/automacao/evidencias/evidencia.png')

TCResult = tls.reportTCResult(4,5,"POC","p","Teste executado com sucesso !!")

a_file=open('/opt/suzanoit/automacao/evidencias/evidencia.png', mode='rb')
newAttachment = tls.uploadTestCaseAttachment(a_file, 4, 5,
            title='PNG Example v1', description='PNG Attachment Example for a TestCase v1')


print("Teste executado")
driver.quit()

sys.exit()
