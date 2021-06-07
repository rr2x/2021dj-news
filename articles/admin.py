from django.contrib import admin
from .models import Article, Comment


class CommentInLine(admin.TabularInline):  # or can use admin.StackedInLine
    model = Comment
    extra = 0  # so that no extra empty forms below the comment list


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
