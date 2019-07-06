import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
login = 'guillaumeoctavio@gmail.com'
password = 'pxsbtpvhlzmluhkl'
conn.ehlo()

conn.starttls()

conn.ehlo()

conn.login(login , password)


def mandamail(a, b, c):

    conn.sendmail(login, a , b + c)
    print('Mensaje Enviado')
    

print('Escriba el destinatario: ')
mail = input()

print('Escriba el asunto: ')
asunto = 'Subject: '+ input() + '\n\n'

print('Escriba el mensaje: ')
mensaje = input()

mandamail(mail, asunto, mensaje)
