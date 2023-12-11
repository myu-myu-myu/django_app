from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pjt1.app1.urls")),
]


from django.contrib.auth.models import Group
admin.site.site_title = "Playlist"
admin.site.site_header = "Playlist 管理サイト"
admin.site.index_title = '参加者の投稿情報を確認してください。'
admin.site.unregister(Group)
admin.site.disable_action('delete_selected')

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)