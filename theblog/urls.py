from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('deteil/<int:pk>/',views.Detail.as_view(),name='deteil'),
    path('add_post/',views.add_post,name='add_post'),
    path('update_post/<int:pk>/',views.UpdatePostView.as_view(),name='update_post'),
]
