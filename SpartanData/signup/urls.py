"""signup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from accounts.views import home_view, login_home_view, activated_view, signup_view, login_view, activation_sent_view, activate, dashboard, analysisChoose, predAnalysis, regAnalysis, dashboardResubmit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_home_view, name="login_home"),
    path('activated/', activated_view, name = "activated"),
    path('home', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('activated/login/', login_view, name = "login"),
    path('dashboard/', dashboard, name="dashboard"),
    path('analysisChoose/', analysisChoose, name="analysisChoose"),
    path('predAnalysis/', predAnalysis, name="predAnalysis"),
    path('regAnalysis/', regAnalysis, name="regAnalysis"),
    path('dashboardResubmit/', dashboardResubmit, name="dashboardResubmit"),
]
