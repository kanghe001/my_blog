from django.contrib import admin
from my_blog.models import *
# Register your models here.

admin.autodiscover()


class ArticalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'desc', 'click_count')
    search_fields = ('title', 'user')
    list_filter = ('user',)
    date_hierarchy = 'date_publish'
    ordering = ('-date_publish',)
    filter_horizontal = ('tag', )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.7/kindeditor-min.js',
            '/static/js/kindeditor-4.1.7/lang/zh-CN.js',
            '/static/js/kindeditor-4.1.7/config.js',
        )



admin.site.register(User)
admin.site.register(Artical, ArticalAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
