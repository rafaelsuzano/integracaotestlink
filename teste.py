
import testlink


SERVER_URL ="http://45.62.235.18:2016//testlink/lib/api/xmlrpc/v1/xmlrpc.php"
DEVKEY = "fb9af0eb240ddc1f6b7cbc9c93527cd9"


tls = testlink.TestlinkAPIClient(SERVER_URL, DEVKEY)
tls.about()
print(tls.countProjects())


