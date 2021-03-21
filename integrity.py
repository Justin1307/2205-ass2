from hashlib import sha256
import pyotp

delimiter = "******"

# client-side

def generateIntegrity(data):

    sha256_result = int(sha256(data.encode('utf-8')).hexdigest(),16)
    return str(sha256_result)

# Server-side

#verification process

def verifyIntegrity(data,msg):

    # Generate the hash of the data
    sha256_result = int(sha256(data.encode('utf-8')).hexdigest(),16)
    print (sha256_result)

    # Verify
    checkResult =  str(sha256_result) == msg

    return checkResult

data = "Hi i am justin"
msg = generateIntegrity(data)
check = verifyIntegrity(data,msg)
print (check)