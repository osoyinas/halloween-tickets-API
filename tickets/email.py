from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from urllib.parse import quote

def notify_ticket_to_admin(ticket):
    context = {'titular':ticket.titular,
            'number':ticket.number,
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
    

QR_API = 'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data='

def send_ticket_to_titular(ticket):

    persons = ticket.persons.all()
    persons_dict = [{'name': person.name, 'url': QR_API + quote(settings.HOST_URL + '/api/tickets/check/' + str(person.id))} for person in persons]
    print(persons_dict)
    context = {'titular':ticket.titular,'persons_dict': persons_dict, 'id':ticket.id }
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
    