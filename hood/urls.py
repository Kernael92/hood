from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^home/',views.home, name='home'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),
    url(r'^setting/', views.profile_setting, name='profile_setting'),
    url(r'^business/',views.business, name='business'),
    url(r'^new/business$', views.new_business, name='new-business'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'post(\d+)',views.post, name='post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)