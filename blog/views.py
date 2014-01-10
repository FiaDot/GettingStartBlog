from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from blog.models import Post
from blog.models import Comment
from django.core.context_processors import csrf
from blog.forms import CommentForm

def main(request):
    """ Main listing """
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 2)
    
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
        
    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
        
    return render_to_response("list.html", dict(posts=posts, user=request.user))        



def post(request, pk):
    """
    post = Post.objects.get(pk=int(pk))
    d = dict(post=post, user=request.user)
    return render_to_response("post.html", d)
    """
    post = Post.objects.get(pk=int(pk))
    comments = Comment.objects.filter(post=post)
    d = dict(post=post, comments=comments, form=CommentForm(), user=request.user)
    d.update(csrf(request))
    return render_to_response("post.html", d)




def add_comment(request, pk):
    """Add a new comment."""
    p = request.POST

    # p.has_key("body")    is deprecated ?
    if p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("blog.views.post", args=[pk]))

