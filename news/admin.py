from django.contrib import admin
from models import Article

# Add this back when we make attachments support optional
# from attachments.admin import AttachmentInlines

class ArticleAdmin(admin.ModelAdmin):
#    inlines = [AttachmentInlines]
    list_display = ('title', 'published', 'created', 'modified', 'slug')
    readonly_fields = ('created', 'modified')

    fieldsets = (
        ('Article Information', {'fields': ('title','body','published')}),
        ('Advanced', {
            'fields': ['author', 'slug', 'created', 'modified', 'summary'],
            'classes': ['collapse',],
        }),
    )

admin.site.register(Article, ArticleAdmin)
