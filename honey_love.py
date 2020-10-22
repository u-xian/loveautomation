from twilio.rest import Client

account_sid = 'AC925b5a5ddb28d7bd7ebdf470aa691117'
auth_token = '0e08124e2630be60fec36976b42d2416'
client = Client(account_sid, auth_token)


def send_love():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Kwambara neza',
        to='whatsapp:+250722123208')
    print(message.sid)
