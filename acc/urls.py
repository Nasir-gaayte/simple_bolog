from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView




urlpatterns = [
    path('register/',views.register_request,name='register'),
    path('login/',views.login_req,name='login'),
    path('logout/',views.logout_request,name='logout'),
    path('edit_profile/',views.UserEditView.as_view(),name='edit_profile'),
    path('password/',PasswordChangeView.as_view(template_name='acc/change_password.html')),
]

