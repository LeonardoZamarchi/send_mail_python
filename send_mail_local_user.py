import win32com.client as win32 #pip install pywin32

def send_mail(dest, subject,body,html, attach):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = dest
    mail.Subject = subject
    mail.Body = body
    mail.HTMLBody = html

    if attach != '':
        mail.Attachments.Add(attach)

    mail.Send()


send_mail(dest,subject,body,html, attach)
