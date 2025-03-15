"""
Views for the Pages app — used to render simple pages
"""
from django.shortcuts import render, get_object_or_404
from .models import Page


def page_detail(request, slug):
    """
    Display an individual :model:`pages.Page`.

    **Context**

    ``page``
        An instance of :model:`pages.Page`.

    **Template:**

    :template:`pages/page_detail.html`
    """

    queryset = Page.objects.filter(status=1)
    page = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "pages/page_detail.html",
        {
            "page": page,
        },
    )
