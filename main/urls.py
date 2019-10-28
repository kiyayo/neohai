from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . import views

app_name='main'

urlpatterns =[
    path('', views.index,name='home'),
    path('profile/', views.profile,name ='profile'),
    path('change-password/',PasswordChangeView.as_view(template_name='main/change-password.html'),name='password_change'),
    path('password_change/done/',PasswordChangeDoneView.as_view(template_name='main/password_change_done.html'),name=' password_change_done'),
    path('password_reset/',PasswordResetView.as_view(template_name='main/password_reset_form.html',email_template_name='main/password_reset_email.html',subject_template_name='main/password_reset_subject.txt',success_url='' ),name='password_reset'),
    path('password_reset/done',PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64/<token>',PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'),name='password_reset_complete'),
    path('profile/edit/',views.edit_profile,name='edit profile'),
    path('register/',views.register, name = 'register'),
    path('login/', LoginView.as_view(template_name='main/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='main/logout.html'),name = 'logout'),
    path('<str:username>/',views.username,name='username'),
    path('keyword/<str:keyword>/',views.keyword, name ='keyword'),
    path('about',views.about,name='about'),
    path('star/<int:pk>/',views.star,name='star'),
    path('search',views.search,name='search'),
    path('starred',views.starred,name='starred'),
    path('feedback',views.feedback,name='feedback'),
    path('gallery',views.gallery,name='gallery'),
    path('service-worker.js',TemplateView.as_view(template_name='main/service-worker.js',content_type='application/x-javascript')),
] 