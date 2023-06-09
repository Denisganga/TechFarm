from django.urls import path

from django.contrib.auth import views as auth_views

from .views import HomePage,Register,Login


app_name = 'auth_system'

urlpatterns = [
    path('home/', HomePage,name="home-page"),  #what have used to connectthe apps
    path('register/',Register,name="register-page"),
    path('login/',Login,name="login-page"),


      path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='auth_system/password_reset.html',
        email_template_name='auth_system/password_reset_email.html',
        subject_template_name='auth_system/password_reset_subject.txt'
    ), name='password_reset'),

path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
    template_name='auth_system/password_reset_done.html'
), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth_system/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth_system/password_reset_complete.html'
    ), name='password_reset_complete'),
    
    ]