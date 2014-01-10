from django.contrib import admin
from blog.models import Post
from blog.models import Comment

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created') 
    
#    , 'body', 'created'
    list_filter = ['created']

    search_fields = ['title']
    
    # 세부 뷰에서 단순 출력 순서
#    fields = ['title', 'body']
    
    # 옵션
"""    fieldsets = [
        ('제목', {'fields': ['title']}),
        ('내용', {'fields': ['body']}),
    ]
"""
              
admin.site.register(Post, PostAdmin)




class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created')
    
admin.site.register(Comment, CommentAdmin)    
    