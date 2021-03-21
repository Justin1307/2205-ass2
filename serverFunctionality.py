from hashlib import sha256
from pynewhope import newhope
class server:
    def __init__(self,message) -> None:
        self.data = message

    def generateAuthSharedKey(self,msg):
        sharedKey, serverMsg = newhope.sharedB(msg)
        return sharedKey,serverMsg

    def __confidentiality(self):
        pass

    def __verifyIntegrity(self,message):
        # Generate the sha256 of the data
        sha256_result = int(sha256(self.data.encode('utf-8')).hexdigest(), 16)
        # checkResult = to_be_verified == sha256_result
        result = str(sha256_result) == message
        return result
