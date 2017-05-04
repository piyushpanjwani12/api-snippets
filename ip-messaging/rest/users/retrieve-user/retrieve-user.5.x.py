# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest.ip_messaging import TwilioIpMessagingClient

# Your Account Sid and Auth Token from twilio.com/user/account
account = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
token = "AUTH_TOKEN"
client = TwilioIpMessagingClient(account, token)

service = client.services.get(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
user = service.users.get(sid="USER_SID")
print(user)
