from django.conf import settings
from django.db import models
from django.utils import timezone
from django.views.generic import ListView


# Create your models here.

class Category(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=400, null=True) 

    def __str__(self):
        return self.nome

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    titulo = models.CharField(max_length=400)
    conteudo = models.CharField(max_length=2000)
    datapublicacao = models.DateTimeField(blank=True, null=True)
    datacriacao = models.DateTimeField(default=timezone.now)
    tag = models.CharField(max_length=50)
    autor = models.CharField(max_length=120)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("data",)
        
    def __str__(self):
        return f"Comentário por {self.autor}"
    
class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category'])
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context