from django.conf.urls import url
from views import RequestView, OptionsView, SearchView, ArtistView, AudioView

urlpatterns = [
    url(r'^request', RequestView.as_view()),
    url(r'^search/options', OptionsView.as_view()),
    url(r'^audio/list', SearchView.as_view()),
    url(r'^add/artist', ArtistView.as_view()),
    url(r'^add/audio', AudioView.as_view())
]