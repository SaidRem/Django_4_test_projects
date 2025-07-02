from django.shortcuts import render
from .models import Article


def articles_list(request):
    template = 'articles/articles_list.html'

    articles = Article.objects.prefetch_related('scopes__tag')

    for article in articles:
        article.sorted_scopes = sorted(
            article.scopes.all(),
            key=lambda s: (not s.is_main, s.tag.name)
        )

    context = {'articles': articles}
    return render(request, template, context)
