from django.core.mail import send_mail
from celery import shared_task
from spam.models import Contact

@shared_task
def send_spam():
    emails = [i.email for i in Contact.objects.all()]
    send_mail(
        '<h1> Py25 shop project <h1/>', # title
        f'hello go to our website'
        'kasimmashrapov@gmail.com', # from
        [emails] # to
    )