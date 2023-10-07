
# cms_app/urls.py

from django.urls import path
from .views import user_register,user_login,home,create_post,create_like,delete_post,update_user,delete_user,user_list, post_list, post_detail

urlpatterns = [
    
    path('',user_register,name='register'),
    path('register/',user_register,name='register'),
    path('login/',user_login,name='login'),
    
    # In this page show all post when user login.  
    path('home/',home,name='home'),
    
    # After login user can create post and like.
    path('create_post/',create_post,name='create_post'),
    path('create_like/<int:post_id>/',create_like,name='create_like'),
    
    # Login user can update and delete their own post.
    path('delete_post/<int:post_id>/',delete_post,name='delete_post'),
    path('update_user/<int:user_id>/',update_user,name='update_user'),
    
    # Delete user via url - /user/
    path('delete_user/<int:user_id>/',delete_user,name="delete_user"),
    
    path('users/', user_list, name='user-list'),
    path('posts/', post_list, name='post-list'),
    
    # Add your other API endpoints here
]
