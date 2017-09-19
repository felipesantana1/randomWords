from django.conf.urls import url
import views
urlpatterns = [

    url(r'^random_word$', views.randomWord),
    url(r'^random_word/new$', views.newRandom),
    url(r'^random_word/reset$', views.attemptReset)

]