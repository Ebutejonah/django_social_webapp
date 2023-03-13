from django.shortcuts import render,redirect
from .forms import ProfileForm
from .models import Search, Profile, Post, LikePost, Follow, Continent, Country, Comments
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from itertools import chain
from django.http import JsonResponse
import random


@login_required()
def indexView(request):
    try:
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)
    except:
        User.DoesNotExist()
        return redirect('/signup')
    
    post = Post.objects.filter(user=request.user.username)                                     
    user_following = Follow.objects.filter(user=request.user.username)
    #getting all the users on the platform
    all_users = User.objects.all()
    #user_object of all those the logged in user is following
    user_following_all = []
    for user_object_following in user_following:
        user_followed = User.objects.get(username = user_object_following.following)
        user_following_all.append(user_followed)
    #User object of all accounts the logged in user is not following
    new_suggestion_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    logged_in_user = User.objects.filter(username = request.user.username)
    #User object of all accounts the logged in user is not following including the logged in user's
    final_suggestion_list = [x for x in list(new_suggestion_list) if (x not in list(logged_in_user))]
    random.shuffle(final_suggestion_list)
    #getting the Profile object from the User instance
    suggested_profile_lists = []
    for users in final_suggestion_list:
        profiles = Profile.objects.filter(user = users)
        suggested_profile_lists.append(profiles)
    suggestion = list(chain(*suggested_profile_lists))
    #getting posts of only users followed by the logged in user and logged in user's posts only
    others_posts = []
    user_posts = []
    for profile in user_following:
        following_post = Post.objects.filter(user = profile.following)
        others_posts.append(following_post)
    all_others_posts = others_posts
    user_posts.append(post)
    all_following_posts=list(chain(*all_others_posts))
    user_post=list(chain(*user_posts))
    joined_posts = all_following_posts + user_post
    if request.method == 'POST':
        if request.FILES.get('postimage') != None and request.POST['caption'] == None:
            post_file = request.FILES.get('postimage')
            post=Post.objects.create(post_file=post_file,user=request.user.username,profile=user_profile)
            post.save()
            return redirect('/')
        elif request.FILES.get('postimage') == None and request.POST['caption'] != None:
            caption = request.POST['caption']
            post=Post.objects.create(caption=caption,user=request.user.username,profile=user_profile)
            post.save()
            return redirect('/')
        else:
            post_file = request.FILES.get('postimage')
            caption = request.POST['caption']
            post = Post.objects.create(post_file=post_file,caption=caption,user=request.user.username,profile=user_profile)
            post.save()
            return redirect('/')
    context = {
                'user_post':post,
                'posts':joined_posts,
                'user_profile':user_profile,
                'other_profiles':suggestion[:4],
                'user_object':user_object,
            }
    return render(request,'index.html',context)


def signUpView(request):
    form = ProfileForm(request.POST or None)
    context={'form':form}
    if request.method == 'POST':
        #getting the details passed in the sign up page
        username = request.POST['username']
        usersname=username.lower()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        #authenticating password & checking if email and username already exist in the database
        if password == password2:
            if User.objects.filter(username=usersname).exists():
                messages.info(request,'Invalid credentials. Please fill form again.')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Invalid credentials. Please fill form again.')
                return redirect('/signup')
            else:
                user=User.objects.create_user(username=usersname,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()

                #creating a profile object once a user successfully signs in
                user_model=User.objects.get(username=usersname)
                profile_obj=Profile.objects.create(user=user_model,id_user=user_model.id,name_first=user_model.first_name,name_last=user_model.last_name)
                profile_obj.save()
                return redirect('/login')
        else:
            messages.info(request,'Passwords must match')
            return redirect('/signup')   
    else:
        return render(request,'signup.html',context)


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        usersname=username.lower()
        password = request.POST['password']
        try:
            account = User.objects.get(username=usersname)
            if password != account.password:
                messages.info(request,'Invalid Username or Password')
        except:
            User.DoesNotExist()
            messages.info(request,'THIS USER DOES NOT EXIST!')
        user = auth.authenticate(username=usersname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
    return render(request,'login.html')

@login_required()
def logoutView(request):
    auth.logout(request)
    return redirect('/login')


@login_required()
def account_settings(request):
    username = request.user.username
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    post=Post.objects.filter(user=user_profile)
    continents = Continent.objects.all()
    context={
                'user_profile':user_profile,
                'post':post,
                'continents':continents,
                'user_object':user_object
            }
    if request.method == 'POST':
        if request.FILES.get('profile_pic') != None and request.FILES.get('bg_pics') == None:
            profile_pics = request.FILES.get('profile_pic')
            background_profile_pics = user_profile.background_profile_pics
            bio = request.POST['bio']
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.bio = bio
            user_profile.save()
            return redirect('/profile/'+username)
        if request.FILES.get('bg_pics') != None and request.FILES.get('profile_pic') == None:
            background_profile_pics = request.FILES.get('bg_pics')
            profile_pics = user_profile.profile_pics
            bio = request.POST['bio']
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.bio = bio
            user_profile.save()
            return redirect('/profile/'+username)
        if request.FILES.get('bg_pics') and request.FILES.get('profile_pic') == None:
            profile_pics = user_profile.profile_pics
            background_profile_pics = user_profile.background_profile_pics
            bio = user_profile.bio
            user_profile.bio = bio
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.save()
            return redirect('/profile/'+username)
        if request.FILES.get('profile_pic') and request.FILES.get('bg_pics') != None:
            profile_pics = request.FILES.get('profile_pic')
            background_profile_pics = request.FILES.get('bg_pics')
            bio = request.POST['bio']
            user_profile.bio = bio
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.save()
            return redirect('/profile/'+username)
        if request.POST['continent'] != None and request.POST['bio'] == None:
            profile_pics = user_profile.profile_pics
            background_profile_pics = user_profile.background_profile_pics
            bio = request.POST['bio']
            get_continents = request.POST.get('continent')
            countries = request.POST.get('country')
            continent = Continent.objects.get(id = get_continents)
            country = Country.objects.get(id = countries)
            user_profile.continent = continent
            user_profile.country = country
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.bio = bio
            user_profile.save()
            return redirect('/profile/'+username)
        if request.POST['bio'] != None and request.POST['continent'] == "Select Continent":
            profile_pics = user_profile.profile_pics
            background_profile_pics = user_profile.background_profile_pics
            bio = request.POST['bio']
            continent = user_profile.continent
            user_profile.continent = continent
            country = user_profile.country
            user_profile.country = country
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.bio = bio
            user_profile.save()
            return redirect('/profile/'+username)
        if request.POST['bio'] == None and request.POST['continent'] == "Select Continent":
            bio = request.POST['bio']
            continent = user_profile.continent
            user_profile.continent = continent
            country = user_profile.country
            user_profile.country = country
            profile_pics = user_profile.profile_pics
            background_profile_pics = user_profile.background_profile_pics
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.bio = bio
            user_profile.save()
            return redirect('/profile/'+username)
        if request.POST['bio'] =="" and request.POST['continent'] == "Select Continent":
            bio = request.POST['bio']
            continent = user_profile.continent
            user_profile.continent = continent
            country = user_profile.country
            user_profile.country = country
            profile_pics = user_profile.profile_pics
            background_profile_pics = user_profile.background_profile_pics
            user_profile.bio = bio
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.save()
            return redirect('/profile/'+username)
        if request.POST['continent'] != None and request.POST['country'] == 'Select Country':
            get_continents = request.POST.get('continent')
            continent = Continent.objects.get(id = get_continents)
            user_profile.continent = continent
            country = None
            user_profile.country = country
            bio = request.POST['bio']
            profile_pics = user_profile.profile_pics
            background_profile_pics = user_profile.background_profile_pics
            user_profile.bio = bio
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.save()
            return redirect('/profile/'+username)
        if request.POST['continent'] and request.POST['country'] != None:
            get_continents = request.POST.get('continent')
            continent = Continent.objects.get(id = get_continents)
            user_profile.continent = continent
            get_country = request.POST.get('country')
            country = Country.objects.get(id = get_country)
            user_profile.country = country
            bio = request.POST['bio']
            profile_pics = user_profile.profile_pics
            background_profile_pics = user_profile.background_profile_pics
            user_profile.bio = bio
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.save()
            return redirect('/profile/'+username)
        if request.POST['bio'] == "":
            bio = request.POST['bio']
            profile_pics = user_profile.profile_pics
            background_profile_pics = user_profile.background_profile_pics
            user_profile.bio = bio
            user_profile.profile_pics = profile_pics
            user_profile.background_profile_pics = background_profile_pics
            user_profile.save()
            return redirect('/profile/'+username)
    return render(request,'settings.html',context)


@login_required()
def likeView(request):
    username = request.user.username
    post_id=request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    liked_post = LikePost.objects.filter(post_id=post_id, username=username).first()
    if liked_post == None:
        new_like = LikePost.objects.create(post_id=post_id,username=username)
        new_like.save()
        post.likes.add(new_like)
        return redirect('/')
    else:
        liked_post.delete()
        post.likes.remove(liked_post)
        post.save()
        return redirect('/')


@login_required()
def CommentView(request,post_id):
    post = Post.objects.get(id = post_id)
    all_comments = Comments.objects.filter(post=post)
    user_object = User.objects.get(username = request.user.username)
    profile = Profile.objects.get(user = user_object)
    if request.method == 'POST':
        comment = request.POST.get('comments')
        new_comment = Comments.objects.create(comments=comment,author=request.user.username,post=post,profile = profile)
        new_comment.save()
        post.no_of_comments += 1
        post.save()
        return redirect('/comments/'+post_id)
    else:
        context = {'post':post,'all_comments':all_comments,'user_object':user_object}
        return render(request, 'comments.html',context)

@login_required()
def deletePost(request):
    post_id=request.GET.get('post_id')
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete()  
    return redirect('/')


@login_required()
def ProfileView(request, username):
    is_following = Follow.objects.filter(user = request.user.username, following = username).first()
    user_object = User.objects.get(username = username)
    user_following = Follow.objects.filter(user = user_object.username)
    user_followers = Follow.objects.filter(following = user_object.username)
    following = len(user_following)
    followers = len(user_followers)
    user_profile = Profile.objects.get(user = user_object)
    post=Post.objects.filter(user=user_profile)
    user_post_length = len(post)
    context={
                'user_profile':user_profile,
                'post':post,
                'user_post_length':user_post_length,
                'following':following,
                'is_following':is_following,
                'followers':followers,
                'user_object':user_object
            }
    return render(request,'profile.html',context)

@login_required()
def FollowersView(request,username):
    user_object = User.objects.get(username = request.user.username)
    user_lists = []
    followers_list = []
    followers_object = Follow.objects.filter(following = username)
    for follower_object in followers_object:
        user_objects = User.objects.filter(username = follower_object.user).first()
        user_lists.append(user_objects)
    for user in user_lists:
        user_profiles = Profile.objects.filter(user = user).first()
        followers_list.append(user_profiles)
    context = {'profiles':followers_list,'user_object':user_object}
    return render(request,'followers.html',context)


@login_required()
def FollowingView(request,username):
    user_object = User.objects.get(username = request.user.username)
    user_lists = []
    following_list = []
    following_objects = Follow.objects.filter(user = username)
    for following_object in following_objects:
        user_objects = User.objects.filter(username = following_object.following).first()
        user_lists.append(user_objects)
    for user in user_lists:
        user_profiles = Profile.objects.filter(user = user).first()
        following_list.append(user_profiles)
    context = {'profiles':following_list,'user_object':user_object}
    return render(request,'following.html',context)


@login_required()
def SearchView(request):
    user_objects = User.objects.filter(username=request.user.username)
    user_object = User.objects.get(username=request.user.username)
    all_users = User.objects.all()
    users_followed = []
    others_profiles = []
    followed = Follow.objects.filter(user = request.user.username)
    for being_followed in followed:
        following = User.objects.get(username=being_followed.following)
        users_followed.append(following)
    users_not_followed = [x for x in list(all_users) if (x not in list(users_followed))]
    #removing the logged in user from the users_not_followed list
    final_users_not_followed = [x for x in list(users_not_followed) if (x not in list(user_objects))]
    #others_users.append(final_users_not_followed)
    for users in final_users_not_followed:
        other_users_profiles = Profile.objects.filter(id_user=users.id)
        others_profiles.append(other_users_profiles)
    other_profiles = list(chain(*others_profiles))
    random.shuffle(other_profiles)
    context = {
            'other_profiles':other_profiles[:4],
            'user_object':user_object
        }
    if request.method == 'POST':
            name = request.POST.get('search')
            searched = Search.objects.create(name = name)
            searched.save()
            return redirect('/searched/'+name)
    else:
        return render(request, 'search.html', context)


@login_required()
def SearchedUserView(request,name):
    user_object = User.objects.get(username = request.user.username)
    users = []
    profiless = []
    user_objects = User.objects.filter(username__icontains = name)
    for user_object in user_objects:
        users.append(user_object.id)
    for ids in users:
        profile = Profile.objects.filter(id_user = ids)
        profiless.append(profile)
    profiless = list(chain(*profiless))
    context = {'profiles':profiless,'name':name,'user_object':user_object}
    return render(request,'searcheduser.html',context)


@login_required()
def followView(request):
    username=request.user.username
    user_object = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_object)
    otheruser_username = request.GET.get('username')
    following_object = User.objects.get(username = otheruser_username)
    following_profile = Profile.objects.get(user=following_object)
    followed = Follow.objects.filter(following=otheruser_username,user=username).first()
    if followed == None:
        following = Follow.objects.create(following=otheruser_username,user=username)
        following.save()
        user_profile.following = following
        following_profile.followers = following
        user_profile.save()
        following_profile.save()
        return redirect('/profile/'+otheruser_username)
    else:
        followed.delete()
        return redirect('/profile/'+otheruser_username)


@login_required()
def CountriesView(request):
    continent = request.GET.get('continent')
    countries = Country.objects.filter(continent = continent)
    context = {'countries':countries}
    return render(request, 'partials/countries.html',context)