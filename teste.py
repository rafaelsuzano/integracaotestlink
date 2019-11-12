
import testlink


SERVER_URL ="http://45.62.235.18:2016//testlink/lib/api/xmlrpc/v1/xmlrpc.php"
DEVKEY = "fb9af0eb240ddc1f6b7cbc9c93527cd9"


tls = testlink.TestlinkAPIClient(SERVER_URL, DEVKEY)
tls.about()
print(tls.countProjects())


TCResult = tls.reportTCResult(4,2,"DEMO","p","passou")
TCResult = tls.reportTCResult(8,2,"DEMO","f","Errado")
TCResult = tls.reportTCResult(10,2,"DEMO","b","bloqueado")




imagem = "C:\\testlink\integracaotestlink\\logo.jpg"




a_file=open(imagem, mode='rb')
newAttachment = tls.uploadTestCaseAttachment(a_file, 4, 1,
            title='PNG Example v1', description='PNG Attachment Example for a TestCase v1')