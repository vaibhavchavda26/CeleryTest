from django.urls import path
from core.views import SendEmail

urlpatterns = [
    path("mail/", SendEmail.as_view(), name="send_email"),
    path("mail/<int:pk>/", SendEmail.as_view(), name="send_email"),
    # path("", send_mail_to_all, name="index")
]
