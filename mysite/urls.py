from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #hottrack.urls 내의 urlpatterns에 prefix로서 hottrack/을 추가
    path(route="hottrack/", view=include("hottrack.urls")),
    
    # / 로 접근시 hottrack/ 주소로 페이지 이동
    path(route="", view=lambda request: redirect("hottrack/")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path(route='__debug__/', view=include(debug_toolbar.urls)),
    ]