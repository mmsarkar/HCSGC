from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com

account_sid = 'ACa693a964c607267e8da5dba7fc8df29c'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18442408072',
  to='+19492947932',
  body="your mom"
)

print(message.sid)