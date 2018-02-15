from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_medical_report_patient(name,receiver, treatment, doctor, patient):
    # Creating message subject and sender
    subject = 'Medical Report'
    sender = 'biinewtondev@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/report_to_patient.txt',{"name": name, 'treatment':treatment, 'doctor':doctor, 'patient':patient})
    html_content = render_to_string('email/report_to_patient.html',{"name": name, 'treatment':treatment, 'doctor':doctor, 'patient':patient})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
