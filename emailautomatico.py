import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>  Meus amigos, Boa noite </p>
    <p>Tenha um otimo dia, Sucesso</p>"""

msg = email.message.Message()
msg["Subject"] = "Motivação diaria"
msg["From"] =
msg["To"] =
password =
msg.add_header("Content-tipy","text-html")
msg.set_payload(corpo_email)

s = smtplib.SMTP ("smtp.gmail.com: S87")
s.starttls()
s.login(msg[from],password)
s.sendmail(msg[from],[msg[To]],msg.as_string().encode("utf-B"))
pRINT("Email enviado")
