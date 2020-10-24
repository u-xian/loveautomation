from twilio.rest import Client

account_sid = 'XXXXXX'
auth_token = 'YYYYY'
client = Client(account_sid, auth_token)


def send_love():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Kwambara neza',
        to='whatsapp:+9999999999999')
    print(message.sid)
