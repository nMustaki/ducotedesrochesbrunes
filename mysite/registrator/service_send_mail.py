import time
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def my_send_mail(visitor, slot_time):

    for i in range(2):
        time.sleep(i + 1)
        try:
            success = send_mail(
                subject="Votre réservation au Jardin des Roches brunes",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[visitor.email],
                fail_silently=False,
                message="Here is the message.",
                html_message=render_to_string(
                    "registrator/confirmation_email.html", {"visitor": visitor, "time": slot_time}
                ),
            )
            if success:
                return True
        except Exception:
            pass
    return False
