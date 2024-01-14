from django.shortcuts import render,redirect
from .models import Friend,Profile,ChatMessage
from .forms import ChatMessageForm,SignUpForm,LoginForm,AddFriendForm
from django.http import JsonResponse, HttpResponse
import json

from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from django.utils import timezone
from django.db.models import Max, F, ExpressionWrapper, fields

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Max,Q,F,Case,When

from django.db.models import Subquery, OuterRef,Value
from django.db.models.functions import Coalesce
from django.db.models import Prefetch
from django.db import models
from datetime import datetime

def custom_404(request, exception):
    return render(request, '404.html', status=404)
@login_required(login_url='login')
def chat(request, pk=None):
    
    user = request.user.profile
    friends = user.friends.all()
    friends = friends.annotate(
        latest_message_timestamp=Subquery(
            ChatMessage.objects.filter(
                Q(msg_sender=user, msg_receiver=OuterRef('profile')) |
                Q(msg_sender=OuterRef('profile'), msg_receiver=user)
            ).order_by('-timestamp').values('timestamp')[:1]
        )
    )
    friends = friends.order_by('-latest_message_timestamp')
    for friend in friends:
        friend.latest_msg = ChatMessage.objects.filter(
            Q(msg_sender=user, msg_receiver=friend.profile) |
            Q(msg_sender=friend.profile, msg_receiver=user)  
        ).last()
   
    if request.method == "POST":
            add_friend_form = AddFriendForm(request.POST)
            if add_friend_form.is_valid():
                friend_username = add_friend_form.cleaned_data['username']
                
                if user.add_friend(friend_username):
                    
                    messages.success(request, f'Friend {friend_username} added successfully.')
                    
                else:
                    messages.error(request, f'Username {friend_username} does not exist.')
                return redirect("chat")
    context = {"user": user, "friends": friends,"add_friend_form":AddFriendForm()}
    if pk:
        friend = Friend.objects.get(profile_id=pk)
        profile = Profile.objects.get(id=friend.profile.id)
        chats = ChatMessage.objects.all()
        rec_chats=ChatMessage.objects.filter(msg_sender=profile,msg_receiver=user,seen=False)
        rec_chats.update(seen=True)
        form = ChatMessageForm()

        if request.method == "POST":
            form = ChatMessageForm(request.POST)
            if form.is_valid():
                chat_message = form.save(commit=False)
                chat_message.msg_sender = user
                chat_message.msg_receiver = profile
                

                chat_message.save()
                return redirect("chat", pk=friend.profile.id)

        context = {"user": user, "friends": friends, "friend": friend, "form": form, "profile": profile, "chats": chats,"num": rec_chats.count(),"add_friend_form": AddFriendForm()}
    
    else:
        
       

        context = {"user": user, "friends": friends,"add_friend_form":AddFriendForm()}
    
    return render(request, 'mychatapp/index.html', context)



def sentMessages(request,pk):
    user=request.user.profile
    friend=Friend.objects.get(profile_id=pk)
    profile=Profile.objects.get(id=friend.profile.id)
    
    data=json.loads(request.body)
    
    new_chats=data["msg"]
    
    new_chat_message=ChatMessage.objects.create(body=new_chats,msg_sender=user,msg_receiver=profile,seen=False)
    new_chat_message.sender_deleted = True
    new_chat_message.save()
    print(new_chats)
    return JsonResponse(new_chat_message.body,safe=False)

def receivedMessages(request,pk):
    user=request.user.profile
    friend=Friend.objects.get(profile_id=pk)
    arr=[]
    profile=Profile.objects.get(id=friend.profile.id)
    chats=ChatMessage.objects.filter(msg_sender=profile,msg_receiver=user,seen=False,sender_deleted=False)
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse(arr,safe=False)
@login_required(login_url='login')
def delete_message(request, pk):
    message = get_object_or_404(ChatMessage, pk=pk)

    # Check if the current user is the sender of the message
    if message.msg_sender == request.user.profile:
        message.delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'You are not allowed to delete this message.'})
def chatNotification(request):
    user=request.user.profile
    friends=user.friends.all()
    friends = friends.annotate(
        latest_message_timestamp=Subquery(
            ChatMessage.objects.filter(
                Q(msg_sender=user, msg_receiver=OuterRef('profile')) |
                Q(msg_sender=OuterRef('profile'), msg_receiver=user)
            ).order_by('-timestamp').values('timestamp')[:1]
        )
    )
    friends = friends.order_by('-latest_message_timestamp')
    arr=[]
    for friend in friends:
        chats=ChatMessage.objects.filter(msg_sender__id=friend.profile.id,msg_receiver=user,seen=False)
        arr.append(chats.count())
    return JsonResponse(arr,safe=False)

def signUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profile.objects.create(user=user, name=user.username)
            
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('chat')  # Redirect to the chat page after registration
    else:
        form = SignUpForm()

    return render(request, 'mychatapp/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat')  # Redirect to the chat page after login
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    if request.user.is_authenticated:
        return redirect('chat')
    return render(request, 'mychatapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
from django.http import JsonResponse

@login_required(login_url='login')
def fetch_friends(request, pk=None):
    if pk:
        user = request.user.profile
        friends = user.friends.filter(pk=pk)
    else:
        # Fetch all friends if pk is not provided
        user = request.user.profile
        friends = user.friends.all()

    friends = friends.annotate(
        latest_message_timestamp=Subquery(
            ChatMessage.objects.filter(
                Q(msg_sender=user, msg_receiver=OuterRef('profile')) |
                Q(msg_sender=OuterRef('profile'), msg_receiver=user)
            ).order_by('-timestamp').values('timestamp')[:1]
        )
    )
   
    friends = friends.order_by('-latest_message_timestamp')
    for friend in friends:
        friend.latest_msg = ChatMessage.objects.filter(
            Q(msg_sender=user, msg_receiver=friend.profile) |
            Q(msg_sender=friend.profile, msg_receiver=user)  
        ).last()

    context = {"user": user, "friends": friends}
    html_response = render_to_string('mychatapp/chat-list.html', context)

    return JsonResponse({'friends_html': html_response})






