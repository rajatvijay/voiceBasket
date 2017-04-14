from django.conf.urls import url
from views import GenericUserView, DashboardView

urlpatterns = [
    url(r'^user', GenericUserView.as_view()),
    url(r'^dashboard', DashboardView.as_view())
]