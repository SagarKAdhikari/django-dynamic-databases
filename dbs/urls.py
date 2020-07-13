from django.conf.urls import include, url
from  .views import *


urlpatterns = [

	url(r'^create-user/(?P<id>.+)/$',CreateUser.as_view()),
	url(r'^post-user/$',CreateSth.as_view()),


]