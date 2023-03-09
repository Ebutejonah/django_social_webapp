from django.urls import path
from .views import CommentView, FollowersView, FollowingView, SearchedUserView, deletePost, indexView, likeView, followView, logoutView, signUpView, loginView,account_settings,likeView,ProfileView, CountriesView, SearchView

app_name = 'core'

urlpatterns = [
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
]

htmx_urlpatterns = [
    path('like-post',likeView,name='like-post'),
    path('delete-post',deletePost,name='delete-post'),
    path('countries', CountriesView, name ='countries')
]

urlpatterns += htmx_urlpatterns