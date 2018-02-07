from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "0000"
# Your Auth Token from twilio.com/console
auth_token  = "0000"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="0000", 
    from_="0000",
    body="Hello from Python!")

print(message.sid)