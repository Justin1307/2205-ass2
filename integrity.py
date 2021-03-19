from hashlib import sha256
import pyotp
import time


# client and server needs to have their own copy of the secret
# base32secret = pyotp.random_base32()
# alternative specify own secret
base32secret = 'S3K3TPI5MYA2M67V'
string_integrity = 'I am a string that needs integrity'
# instanciate totp
totp = pyotp.TOTP(base32secret)
# combine string and otp for hashing
to_integrity = string_integrity + totp.now()



# test the hash
print(sha256(to_integrity.encode('utf-8')).hexdigest())


#verification process
otp_val = totp.now()
# concatenate the decrypted string msg with otp value
msg_received = string_integrity + otp_val
# then sha256 it
print(sha256(msg_received.encode('utf-8')).hexdigest())

