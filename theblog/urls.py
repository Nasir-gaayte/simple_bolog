from django.urls import path
from theblog import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('deteil/<int:pk>/',views.Detail.as_view(),name='deteil'),
    path('add_post/',views.add_post,name='add_post'),
    path('update_post/<int:pk>/',views.UpdatePostView.as_view(),name='update_post'),
    path('delete_post/<int:pk>',views.DeletePostView.as_view(),name='delete_post'),
    path('add_category/',views.add_cotegory,name='add_category'),
    path('detail_category/<int:pk>/',views.DetailCategory.as_view(),name='detail_category'),
    path('category_list/<str:cats>/',views.CategoryView,name='category_list'),
    path('like/<int:pk>',views.LikeView,name='like_post'),
    path('comment/<int:pk>/',views.CommentView.as_view(),name='comment'),
    # path('comment/',views.add_comment,name='comment'),
]
