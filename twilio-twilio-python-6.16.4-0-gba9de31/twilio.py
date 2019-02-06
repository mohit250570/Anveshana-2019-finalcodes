import time
from sinchsms import SinchSMS
number='7557462911'
message="hi"
client=SinchSMS("b2557e0e-1512-4953-a99b-c543d96f9a94","RnEHiZmMBEOmIrdvrbx2mg==")
print("sending '%s' to %s "(message,number))
response = client.send_message(number,message)
