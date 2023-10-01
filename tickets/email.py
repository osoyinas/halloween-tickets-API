from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from urllib.parse import quote

def notify_ticket_to_admin(ticket):
    context = {'titular':ticket.titular,
            'price':ticket.price,
            'date':ticket.date, 
            'url': f"{settings.HOST_URL}/admin/tickets/ticket/{ticket.id}",
            'companions': ticket.persons.all()}
    html_content = render_to_string("email_admin_notify.html",context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        #subject
        f'Nueva reserva de {ticket.titular}',
        #content
        text_content,
        #from email
        settings.EMAIL_HOST_USER,
        #rec list
        settings.ADMIN_MAILS
        )
    email.attach_alternative(html_content,"text/html")
    email.send()
    

QR_API = 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data='

def send_ticket_to_titular(ticket):
    url_check = settings.HOST_URL + 'admin/tickets/ticket/'+ ticket.id
    context = {'titular':ticket.titular,'qr': f"{QR_API}{quote(url_check, safe='')}", 'id':ticket.id }
    html_content = render_to_string("email_template.html",context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        #subject
        'ENTRADA PARA HALLOWEEN-13',
        #content
        text_content,
        #from email
        settings.EMAIL_HOST_USER,
        #rec list
        [ticket.email]
        )
    email.attach_alternative(html_content,"text/html")
    email.send()
    