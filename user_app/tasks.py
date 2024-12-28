import logging
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from beta_survey_django.celery import app


@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'Verify your Snwolley Account',
            '''Dear %s,\n
            Thank you for registering

            Kindly follow this link to verify your account: http://a.com%s

            Regards
            X''' % (str(user.full_name),
                                      reverse('verify', kwargs={'uuid': str(user.verification_uuid)})),
            'X',
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
