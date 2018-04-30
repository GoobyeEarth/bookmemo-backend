from django.conf.urls import url
from users.views import AuthRegister

urlpatterns = [
    url(r'^register/$', AuthRegister.as_view()),
]
