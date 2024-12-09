import smtplib ,ssl

host="smtp.gmail.com"
port=465

#your email , recommend using  gmail app password
username=""
password=""

#enter receiver's email 
receiver=""
context=ssl.create_default_context()

def send_news(messages):
    with smtplib.SMTP_SSL(host=host,port=port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,messages)
        server.quit()
