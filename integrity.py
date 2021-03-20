from hashlib import sha256
import pyotp

delimiter = "******"

# client-side
data = 'I am a string that needs integrity'

# Generate the OTP and sha256 of the data
OTP = int(pyotp.random_hex(),16)
sha256_result = int(sha256(data.encode('utf-8')).hexdigest(),16)

# XOR the OTP and the sha256_result, append the delimiter and the OTP to the back 
integrityResult = str(sha256_result ^ OTP)
data_msg = integrityResult + delimiter + str(OTP)

# Server-side

#verification process

# Split the data according to the delimiter
dataSplit = data_msg.split(delimiter)
integrityResult = int(dataSplit[0])
OTP = int(dataSplit[1])

# XOR the result to get back the hash
to_be_verified = integrityResult ^ OTP

# Verify
print(to_be_verified==sha256_result)

