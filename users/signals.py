from .models import CustomUser
from django.conf import settings
from django.dispatch import receiver
from axes.signals import user_locked_out
import yagmail
from yagmail import YagConnectionClosed
import socket
  

@receiver(user_locked_out)
def handle_brute_force_attack(sender, request, **kwargs):
    
    admin_users = [user.email for user 
                in CustomUser.objects.filter(is_admin=True) ]
    
    subject = "Illegal Login Attempt In your Data App"
    email_sender = 'akarulamstanley@gmail.com'
    email_password = 'dvcpqdqzmizvvckt'
    headers = {
        "From": "Data App Notification"
    }
    
    try:
        yag = yagmail.SMTP(email_sender, email_password)
        contents = f'A BRUTE FORCE attack has been detected in your Data App,\n\
            \nCopy this link to your browser to reset your password: \n<a>{request.META.get("HTTP_HOST")}/users/password_reset</a> '
        yag.send(admin_users, subject, contents, headers=headers)
        
    except socket.error:
        print('Connection error')

