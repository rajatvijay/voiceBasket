from django.conf.urls import url
from views import GenericUserView

urlpatterns = [
    url(r'^user', GenericUserView.as_view())
]