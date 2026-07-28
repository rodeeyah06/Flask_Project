from flask_mail import Message
from extension import mail

def send_verification_email(email,fullname,verification_link):
    msg = Message(
        subject="Verification Email",
        recipients=[email],
    )
    msg.body = f'''
    Hello {fullname},
    Thank you for registering.
    Click the link below to verify your email.
    
    {verification_link}
    
    If you did not register, please Ignore this email.
    
    Regards,
    Rodeeyah Xx 
    '''

    mail.send(msg)