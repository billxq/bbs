from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from post.post_service import build_topic_base_info, bulid_topic_detail_info
from post.models import Topic, Comment


def hello_django_bbs(request):
    html = '<h1>Hello, Django BBS!</h1>'
    return HttpResponse(html)


def topic_list_view(request):
    topic_qs = Topic.objects.all()
    result = {
        'count': topic_qs.count(),
        'info': [build_topic_base_info(topic) for topic in topic_qs]
    }
    return JsonResponse(result)


def topic_detail_view(request, topic_id):
    results = {}
    try:
        results = bulid_topic_detail_info(Topic.objects.get(pk=topic_id))
    except Topic.DoesNotExist:
        pass
    return JsonResponse(results)


# 给话题增加评论的视图函数
def add_comment_to_topic_view(request):
    topic_id = int(request.POST.get('id', 0))
    content = request.POST.get('content', '')
    topic = None

    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        pass

    if topic and content:
        return JsonResponse({'id': add_comment_to_topic(topic, content).id})
    return JsonResponse({})
