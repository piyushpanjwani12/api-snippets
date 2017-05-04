require 'twilio-ruby'

# Get your Account SID and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'AUTH_TOKEN'
service_sid = 'ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
@client = Twilio::REST::Client.new(account_sid, auth_token)

# Retrieve the service
service = @client.chat.v2.services(service_sid).fetch
puts "Chat service #{service_sid} has Friendly Name \"#{service.friendly_name}\""
