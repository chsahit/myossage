from twilio.rest import TwilioRestClient
import sys

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC406175eae41cf573d205e6cfa795a6a8"
auth_token  = "564fe2c40448359123e21fbe46b7631f "
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body=sys.argv[1], from_ ="+19085096113",to="+19088874698") 
# Replace with your Twilio number
print message.sid
