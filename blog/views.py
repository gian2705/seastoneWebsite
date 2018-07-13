from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from home.models import Company
from .models import Post
from property.models import Property
# Create your views here.


class PostViews:

    def post_view(request):
        posts = Post.objects.all().order_by("-timestamp")
        company = Company.objects.all()
        propert = Property.objects.all()
        searchq = search(request)
        if searchq:
            posts = Post.objects.filter(Q(title__icontains=searchq) | Q(content__icontains=searchq) |
                                        Q(user_post__first_name__icontains=searchq) |
                                        Q(user_post__last_name__icontains=searchq)).distinct()

        paginator = Paginator(posts, 4) # 4 posts per page
        page = page_get(request)
        posts = paginator.get_page(page)

        return render(request, "blog.html", context={"posts": posts, "company_details": company, "properties": propert})

    def post_detail(request, id):
        post = get_object_or_404(Post, id=id)
        propert = Property.objects.all()
        company = Company.objects.all()
        return render(request, "single-blog.html", context={"post": post, "properties": propert, "company_details": company})


def search(request):
    search = request.GET.get('search')
    return search


def page_get(request):
    return request.GET.get('page')