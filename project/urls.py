from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


#USER
    url(r'^signup/$','main.views.sign_up'),
    url(r'^signin/$','main.views.signin_view'),
    url(r'^profile_page/$','main.views.profile_page'),
    url(r'^logout/$','main.views.logout_view'),
    url(r'^edit_profile/$','main.views.edit_profile'),



#Game
    url(r'^create_game/$','main.views.create_game'),
    url(r'^game_list/$','main.views.game_list'),
    url(r'^game_detail/(?P<pk>[0-9]+)/$','main.views.game_detail'),


#Game Result
    url(r'^create_game_result/(?P<pk>[0-9]+)/$','main.views.create_game_result'),


]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
