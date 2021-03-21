from hashlib import sha256
from pynewhope import newhope

class client:

    def __init__(self,data) -> None:
        self.data = data

    def generateAuthPrivKey(self):
        privKey, msg = newhope.keygen()
        return privKey,msg

    def generateAuthSharedKey(self,msg,privKey):
        sharedKey = newhope.sharedA(msg,privKey)
        return sharedKey
    
    def __confidentiality(self):
        pass

    def __generateIntegrity(self,data):
        # Generate the sha256 of the data
        sha256_result = int(sha256(data.encode('utf-8')).hexdigest(), 16)
        result = str(sha256_result)
        return result
