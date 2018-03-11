from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[ 
    url(r'^post$',views.post_list,name='post_list'),
    url(r'^create$',views.post_create,name='post_create'),
    url(r'^(?P<id>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^(?P<id>\d+)/update$',views.post_update,name='post_update'),
    url(r'^(?P<id>\d+)/delete$',views.post_delete,name='post_delete'),
    url(r'^list$',views.profile_list,name='profile_list'),
    url(r'^$',views.profile_create,name='profile_create'),
    url(r'^(?P<id>\d+)/details$',views.profile_detail,name='profile_detail'),
    url(r'^(?P<id>\d+)/edit$',views.profile_update,name='profile_update'),
    url(r'^(?P<id>\d+)/cancel$',views.profile_delete,name='profile_delete'),
   
    # url(r'^get$',views.get_post_by_id,name='get_post_by_id'),
    # url(r'^profile/',views.profile,name ='profile'),
    # url(r'^new/profile$', views.new_profile, name='new-profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)