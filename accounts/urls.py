from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("accounts/", views.main, name="main"),
    path("accounts/index/", views.index, name="index"),
    # 회원가입
    path("accounts/signup/", views.signup, name="signup"),
    # 로그인
    path("accounts/login/", views.login, name="login"),
    # 로그아웃
    path("accounts/logout/", views.logout, name="logout"),
    # 회원정보디테일
    path("accounts/<int:pk>/", views.detail, name="detail"),
    # 회원수정
    path("accounts/update/", views.update, name="update"),
    # path('', views.login, name='login'),
    # path('', views., name=''),
    # path('', views., name=''),
    # path('', views., name=''),
]
