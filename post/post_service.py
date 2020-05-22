from post.models import Comment, Topic

def build_topic_base_info(topic):
    return {
        'id': topic.id,
        'title': topic.title,
        'user': topic.user.username,
        'created_time':
            topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
    }


def build_comment_info(comment):
    return {
        'id': comment.id,
        'content': comment.content,
        'up': comment.up,
        'down': comment.down,
        'created_time': comment.created_time.strftime('%Y-%m-%d %H:%M:%S'),
        'last_modified': comment.last_modified.strftime('%Y-%m-%d %H:%M:%S')
    }


def bulid_topic_detail_info(topic):
    comment_qs = Comment.objects.filter(topic=topic)
    return {
        'id': topic.id,
        'title': topic.title,
        'content': topic.content,
        'user': topic.user.username,
        'created_time': topic.created_time.strftime('%Y-%m-%d %H:%M:%S'),
        'last_modified': topic.last_modified.strftime('%Y-%m-%d %H:%M:%S'),
        'comments': [build_comment_info(comment) for comment in comment_qs]
    }
