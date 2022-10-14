from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    #회원가입
    path('signup/', views.signup, name='signup'),
    #로그인
    # path('', views.login, name='login'),
    #로그아웃
    # path('', views., name=''),
    #회원수정
    # path('', views., name=''),
    #회원정보디테일
    # path('', views., name=''),
]
