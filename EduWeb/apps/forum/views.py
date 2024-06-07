from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Forum, Message
from .forms import ForumForm, MessageForm
from apps.users.models import User, Classroom


class ForumView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {"message": "Hello, Forum!"}
        return Response(data)

@login_required
def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum/forum_list.html', {'forums': forums})

@login_required
def forum_detail(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    messages = forum.messages.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.forum = forum
            message.save()
            return redirect('forum_detail', pk=forum.pk)
    else:
        form = MessageForm()
    return render(request, 'forum/forum_detail.html', {'forum': forum, 'messages': messages, 'form': form})

@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.author = request.user
            forum.classroom = request.user.classrooms.first()  # Assuming the user has one classroom
            forum.save()
            return redirect('forum_list')
    else:
        form = ForumForm()
    return render(request, 'forum/create_forum.html', {'form': form})

@login_required
def delete_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    forum_pk = message.forum.pk
    if request.user == message.author or request.user == message.forum.author:
        message.delete()
    return redirect('forum_detail', pk=forum_pk)
