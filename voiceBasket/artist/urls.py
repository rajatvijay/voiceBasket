from django.conf.urls import url
from views import RequestView, OptionsView, SearchView

urlpatterns = [
    url(r'^request', RequestView.as_view()),
    url(r'^search/options', OptionsView.as_view()),
    url(r'^audio/list', SearchView.as_view())
]