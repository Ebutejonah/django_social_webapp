from django.urls import path
from .views import likeView,CommentView, delete_accountview, confirm_delete_accountview, FollowersView
from .views import registeredview, FollowingView, SearchedUserView, deletePost, indexView, followView, logoutView, signUpView, loginView,account_settings,ProfileView, SearchView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('like-post/', likeView, name ='like-post'),
    path('', indexView, name ='home'),
    path('signup/',signUpView, name='signup'),
    path('registered/', registeredview, name='registered'),
    path('login/',loginView, name='login'),
    path('settings/',account_settings,name='settings'),
    path('logout/',logoutView,name='logout'),
    path('profile/<str:username>/',ProfileView, name = 'profile'),
    path('profile/<str:username>/followers/',FollowersView, name = 'followers'),
    path('profile/<str:username>/following/',FollowingView, name = 'following'),
    path('follow/<str:otherusername>/',followView,name='follow'),
    path('search/', SearchView, name = 'search'),
    path('searched/<str:name>/', SearchedUserView, name = 'searched'),
    path('comments/<str:post_id>/', CommentView, name = 'comments'),
    path('delete-post/',deletePost,name='delete-post'),
    # path('json/',indexView,name='json'),
    path('delete_account/', delete_accountview,name="delete_account"),
    path('confirm_delete_account/',confirm_delete_accountview,name="confirm_delete_account"),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'registration/password_change.html'), 
        name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'registration/password_changed.html'), 
        name='password_change_done'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/reset_email.html'), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/reset_complete.html'),
     name='password_reset_complete'),

]
