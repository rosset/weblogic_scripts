import os
import weblogic.security.internal.SerializedSystemIni
import weblogic.security.internal.encryption.ClearOrEncryptedService
 
def decryptString(domainPath, encryptedString):
    es = weblogic.security.internal.SerializedSystemIni.getEncryptionService(domainPath)
    ces = weblogic.security.internal.encryption.ClearOrEncryptedService(es)
    decryptedString = ces.decrypt(encryptedString)
    print "=" * 40
    print " " * 10 +"Decrypted Password:" + decryptedString
    print "=" * 40
 
try:
    os.system('clear')
    if len(sys.argv) == 3:
        decryptString(sys.argv[1], sys.argv[2])
    else:
        print "=" * 40
        print "INVALID ARGUMENTS"
        print "Usage: java weblogic.WLST %s <ABSOLUTE DOMAIN_HOME PATH> <ENCRYPTED_PASSWORD>" %sys.argv[0]
        print "e.g.:"
        print "    java weblogic.WLST %s /oracle/Middleware/11g/user_projects/domains/domain_test/ {AES}xxx-hash-xxx" %sys.argv[0]
        print "=" * 40
except:
    print "Unexpected error: ", sys.exc_info()[0]
    dumpStack()
    raise
