# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Initialize the client
account = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
token = "AUTH_TOKEN"
client = Client(account, token)

credential = client.chat.credentials("CREDENTIAL_SID").fetch()

print(credential.sid)
