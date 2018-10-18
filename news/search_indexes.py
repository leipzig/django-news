from haystack import indexes
from .models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    summary = indexes.CharField(model_attr='summary')
    slug = indexes.CharField(model_attr='slug')
    author = indexes.CharField(model_attr='author')
    categories = indexes.CharField(model_attr='category')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
