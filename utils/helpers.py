from users.models import User

def update_verification_link(user: User):
    user.email_verification_link = ""
    user.save(update_fields=['email_verification_link'])
