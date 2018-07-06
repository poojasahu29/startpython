from django.conf.urls import url
from .import views

urlpatterns = [
 url(r'^$',views.home, name="index"),
    url(r'detail/(?P<e_id>[0-9]+)/$',views.detail, name="detail"),
			#url(r'about/',views.about),
			
]
