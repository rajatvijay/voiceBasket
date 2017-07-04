from django.conf.urls import url
from views import GenericUserView, DashboardView, AcceptRejectRequest

urlpatterns = [
    url(r'^user', GenericUserView.as_view()),
    url(r'^dashboard', DashboardView.as_view()),
    url(r'^update-status', AcceptRejectRequest.as_view())
]