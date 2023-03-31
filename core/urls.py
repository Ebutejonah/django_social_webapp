from django.urls import path
from .views import likeView,CommentView, FollowersView, FollowingView, SearchedUserView, deletePost, indexView, followView, logoutView, signUpView, loginView,account_settings,ProfileView, CountriesView, SearchView

app_name = 'core'

urlpatterns = [
    path('like-post', likeView, name ='like-post'),
    path('', indexView, name ='home'),
    path('signup',signUpView, name='signup'),
    path('login',loginView, name='login'),
    path('settings',account_settings,name='settings'),
    path('logout',logoutView,name='logout'),
    path('profile/<str:username>/',ProfileView, name = 'profile'),
    path('profile/<str:username>/followers',FollowersView, name = 'followers'),
    path('profile/<str:username>/following',FollowingView, name = 'following'),
    path('follow',followView,name='follow'),
    path('search', SearchView, name = 'search'),
    path('searched/<str:name>/', SearchedUserView, name = 'searched'),
    path('comments/<str:post_id>/', CommentView, name = 'comments'),
    path('countries', CountriesView, name ='countries'),
    path('delete-post',deletePost,name='delete-post'),
    path('json',indexView,name='json'),
]
