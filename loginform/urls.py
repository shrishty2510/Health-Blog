"""loginform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from core import views
from blog import views as bg
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='home'),
    path('register/',views.sign_up,name='Sign'),
    path('login/',views.loginform,name='login'),
    path('logout/',views.logoutform,name='logout'),
    path('profile/',views.profilepage,name='profile'),
    path('userprofile/',views.userprofilepage,name='userprofile'),
    path('table/',views.showpost ,name='table'),
    path('table1/',views.showpost1 ,name='table2'),
    path('table2/',views.showpost2 ,name='table3'),
    path('table3/',views.showpost3 ,name='table4'),
    path('usertable/',views.userpost ,name='usertable'),
    path('usertable1/',views.userpost1 ,name='usertable1'),
    path('usertable2/',views.userpost2 ,name='usertable2'),
    path('usertable3/',views.userpost3 ,name='usertable3'),
    path('post/',views.addpost,name='add'),
    path('blogpost/<int:id>/',views.particular,name='pblog'),
    path('delete/<int:id>/',views.delete_data,name='Delete'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)