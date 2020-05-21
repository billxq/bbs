from django.contrib import admin
from .models import Comment, Topic


admin.site.register(Comment)
# admin.site.register(Topic)


# 修改动作菜单，即action
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    actions = ['topic_online', 'topic_offline']
    # 修改changelist的显示列, 除了接收models中定义的字段外，还可以接收自定义的函数
    # 如topic_content和topic_is_online
    list_display = ('title', 'topic_content', 'topic_is_online', 'user',
                    'created_time')
    # 利用search_fields给changelist添加搜索框
    search_fields = ['title', 'user__username']
    # 利用list_filter给ChangeList添加过滤器
    list_filter = ['title', 'user__username', 'is_online']
    # 利用ordering重新定义Model实例的顺序
    ordering = ['is_online', 'id']
    # 分页相关的属性
    # list_per_page = 1   # 默认为100
    # list_max_show_all = 2   # 一共有3条数据，这里最大显示2，所以不会出现“显示全部”
    # 利用fields自定义显示Model的字段,隐藏一些敏感的字段或者不需要显示的字段
    # 而exclude则和fields的功能相反，它会屏蔽里面的字段
    # fields = ['user', 'title', 'is_online']
    # fields的小技巧, user和title会显示在一样上
    fields = [('user', 'title'), 'content', 'is_online', 'content_length']
    # 利用readonly_fields将字段设为只读字段
    readonly_fields = ('title', 'content_length')
    # 利用raw_id_fields降低数据库检索开销
    raw_id_fields = ('user',)

    # 设置只读字段content_length
    def content_length(self, obj):
        return len(obj.content)
    content_length.short_description = u'话题内容长度'

    # 根据is_online字段返回是或否
    def topic_is_online(self, obj):
        return u'是' if obj.is_online else u'否'
    topic_is_online.short_description = u'话题是否在线'  # 列标题

    # 截取content字段前30个字符
    def topic_content(self, obj):
        return obj.content[:30]
    topic_content.short_description = u'话题内容'   # 列标题

    def topic_online(self, request, queryset):
        rows_updated = queryset.update(is_online=True)
        self.message_user(request, '%s topics online' % rows_updated)
    topic_online.short_description = u'上线所选的 %s' % Topic._meta.verbose_name

    def topic_offline(self, request, queryset):
        rows_updated = queryset.update(is_online=False)
        self.message_user(request, '%s topics offline' % rows_updated)
    topic_offline.short_description = u'下线所选的 %s' % Topic._meta.verbose_name
