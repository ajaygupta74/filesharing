import random
import string
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


def generate_random_string(length=20):
    """Generate a random string of specified length consisting of letters."""
    letters = string.ascii_letters  # Includes both uppercase and lowercase letters
    return ''.join(random.choice(letters) for _ in range(length))


def send_verification_mail(email):
    verify_token = generate_random_string()
    link = f"{settings.BASE_URL}{reverse('verify_email', args=[verify_token])}"
    send_mail(
        settings.EMAIL_VERIFY_SUBJECT,
        settings.EMAIL_VERIFY_BODY.format(link=link),
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False)
    return verify_token
    
