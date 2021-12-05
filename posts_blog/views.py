from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .forms import NewCommentForm
# Create your views here.

class HomeView(ListView):
    model=Post
    template_name = 'posts_blog/lista_posts.html'
    context_object_name = 'posts'
    
class CreatePostView(CreateView):
    model=Post
    template_name = 'posts_blog/novo_post.html'
    fields = ['titulo','conteudo']
    
    def get_success_url(self):
        return reverse('detalhe_post', kwargs={'pk': self.object.pk,})
    
class PostEditView(UpdateView):
    model = Post
    template_name = 'posts_blog/atualiza_post.html'
    fields = ['titulo','conteudo']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts_blog/delete_post.html'
    success_url = reverse_lazy('home')
    
def post_single(request, pk):

    post = get_object_or_404(Post, pk=pk)

    comments = post.comments.filter(post_id=pk).order_by('-pk')

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect(reverse('detalhe_post', args=(pk, )))
    else:
        comment_form = NewCommentForm()
    return render(request, 'posts_blog/detalhe_post.html', {'post': post, 'comments':  user_comment, 'comments': comments, 'comment_form': comment_form})

def cria_comentario(request, pk):

    post = get_object_or_404(Post, pk=pk)

    comments = post.comments.filter(post_id=pk).order_by('-pk')

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect(reverse('detalhe_post', args=(pk, )))
    else:
        comment_form = NewCommentForm()
    return render(request, 'posts_blog/cria_comentario.html', {'post': post, 'comments':  user_comment, 'comments': comments, 'comment_form': comment_form})

class CatListView(ListView):
    template_name = 'posts_blog/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__nome=self.kwargs['category'])
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context