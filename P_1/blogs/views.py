from django.shortcuts import render, get_object_or_404 ,redirect
from blogs.models import Blog , Comment

def blogs(request):
    blogha = Blog.objects.all()
    context ={

        "blogs":blogha,
    }
    return render(request,'blogs.html',context)

# def render_comment (request) :
#     comment = Comment.objects.all()

#     return render(request,'blog.html',{'commentha':comment})
    
def render_blog (request,post) :
    article = Blog.objects.get(slug=post)
    comments = Comment.objects.filter(blog=article,published=True)
    # comments = article.comments.all()
    
    if request.method == 'POST':
        try:
            Comment.objects.create(
                name=request.POST['name'],
                subject=request.POST['subject'],
                email=request.POST['email'],
                comment=request.POST['message'],
                image=request.FILES['img'],
                blog = article
            )
        except:
            Comment.objects.create(
                name=request.POST['name'],
                subject=request.POST['subject'],
                email=request.POST['email'],
                comment=request.POST['message'],
                blog = article
            )

        return redirect('blog',post)
    elif request.method == 'GET':
        return render(request,'blog.html',{'article': article,'commentha':comments})

