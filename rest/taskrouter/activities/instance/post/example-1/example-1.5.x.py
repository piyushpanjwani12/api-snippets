# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioTaskRouterClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
workspace_sid = "WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
activity_sid = "WAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = TwilioTaskRouterClient(account_sid, auth_token)

activity = client.activities(workspace_sid).update(activity_sid,friendly_name='NewAvailableFriendlyName',available='true')
print(activity.friendly_name)

# alternatively
activity = client.activities(workspace_sid).get(activity_sid)
activity = activity.update(friendly_name='NewAvailableFriendlyName')
print(activity.friendly_name)