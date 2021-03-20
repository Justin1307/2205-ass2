from hashlib import sha256
import pyotp

delimiter = "******"

# client-side

def generateIntegrity(data):

    # Generate the OTP and sha256 of the data
    OTP = int(pyotp.random_hex(),16)
    sha256_result = int(sha256(data.encode('utf-8')).hexdigest(),16)

    # XOR the OTP and the sha256_result, append the delimiter and the OTP to the back 
    integrityResult = str(sha256_result ^ OTP)
    data_msg = integrityResult + delimiter + str(OTP)
    return data_msg

# Server-side

#verification process

def verifyIntegrity(data,msg):

    # Split the data according to the delimiter
    dataSplit = data.split(delimiter)
    integrityResult = int(dataSplit[0])
    OTP = int(dataSplit[1])

    # Generate the hash of the data
    sha256_result = int(sha256(msg.encode('utf-8')).hexdigest(),16)

    # XOR the result to get back the hash
    to_be_verified = integrityResult ^ OTP

    # Verify
    checkResult = to_be_verified == sha256_result

    return checkResult

data = "Hi i am justin"
data_msg = generateIntegrity(data)
check = verifyIntegrity(data_msg,data)
print (check)