from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Post, Like, Comment, Follow
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration successful!")
        return redirect("login")

    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    users = User.objects.exclude(id=request.user.id)
    following_ids = list(Follow.objects.filter(follower=request.user).values_list("following_id", flat=True))

    return render(
        request,
        "home.html",
        {
            "posts": posts,
            "users": users,
            "following_ids": following_ids
        }
    )

def profile(request):
    user = request.user

    followers_count = Follow.objects.filter(following=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    posts_count = Post.objects.filter(user=user).count()

    return render(
        request,
        "profile.html",
        {
            "profile_user": user,
            "followers_count": followers_count,
            "following_count": following_count,
            "posts_count": posts_count,
        }
    )

def events(request):
    return render(request, "events.html")

def announcements(request):
    return render(request, "announcements.html")

def clubs(request):
    return render(request, "clubs.html")

def coding(request):
    return render(request, "coding.html")

def join_coding(request):
    if request.method == "POST":
        return render(request, "join_success.html", {"club_name": "Coding Club"})

    return render(request, "join_coding.html")

def cultural(request):
    return render(request, "cultural.html")

def join_cultural(request):
    if request.method == "POST":
        return render(request, "join_success.html", {"club_name": "Cultural Club"})

    return render(request, "join_cultural.html")

def create_post(request):
    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            Post.objects.create(
                user=request.user,
                content=content
            )
            return redirect("home")

    return render(request, "create_post.html")

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        like.delete()

    return redirect("home")

def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        text = request.POST.get("text")

        if text:
            Comment.objects.create(
                user=request.user,
                post=post,
                text=text
            )

    return redirect("home")

@login_required
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)

    if user_to_follow != request.user:
        Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

    return redirect("home")

def sports(request):
    return render(request, "sports.html")

def join_sports(request):
    if request.method == "POST":
        return render(request, "join_success.html", {"club_name": "Sports Club"})

    return render(request, "join_sports.html")

def literary(request):
    return render(request, "literary.html")

def join_literary(request):
    if request.method == "POST":
        return render(request, "join_success.html", {"club_name": "Literary Club"})

    return render(request, "join_literary.html")

def robotics(request):
    return render(request, "robotics.html")

def join_robotics(request):
    if request.method == "POST":
        return render(request, "join_success.html", {"club_name": "Robotics Club"})

    return render(request, "join_robotics.html")
