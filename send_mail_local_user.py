import win32com.client as win32

def send_mail(to, subject, body, html, attach):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    mail.Body = body
    mail.HTMLBody = html
    if attach != '':
        mail.Attachments.Add(attach)
    
    try:
        mail.Send()
        print('Your message was sent successfully.')
    except:
        print('ERROR: failed delivery message.')


#specifies the path of the csv file with the email sending schedules with the structure
#to,subject,body,attach,html
scheduler = pd.read_csv('mail_schedule.csv')
for index, row in scheduler.iterrows():
    to= row[0]
    subject= row[1]
    body= row[3]
    #html's optional
    with open(row[4],'r', encoding='ISO-8859-1') as f:
        html= f.read()
    attach = ''
    send_mail(to,subject,body,html, attach)
