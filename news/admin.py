from django.contrib import admin
from models import Article

# Add this back when we make attachments support optional
# from attachments.admin import AttachmentInlines

class ArticleAdmin(admin.ModelAdmin):
#    inlines = [AttachmentInlines]
    list_display = ('title', 'published', 'created', 'modified', 'markup_filter', 'slug')
    readonly_fields = ('created', 'modified')

    fieldsets = (
        ('Article Information', {'fields': ('title','body','published')}),
        ('Advanced', {
            'fields': ['markup_filter', 'author', 'slug', 'created', 'modified', 'summary'],
            'classes': ['collapse',],
        }),
    )

admin.site.register(Article, ArticleAdmin)
