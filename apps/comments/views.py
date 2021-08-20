from django.shortcuts import render
from apps.comments.models import Reply


def index_reply(requset):
    reply = Reply.objects.all()
    return render(requset, 'replies/index_reply.html', locals())
