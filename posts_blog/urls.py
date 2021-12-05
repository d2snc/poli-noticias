from django.urls import path
from .views import HomeView,CreatePostView,PostEditView,PostDeleteView
from . import views

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('noticia/<int:pk>/',views.post_single,name="detalhe_post"),
    path('post/novo/',CreatePostView.as_view(),name="novo_post"),
    path('noticia/<int:pk>/editar/',PostEditView.as_view(),name="atualiza_post"),
    path('noticia/<int:pk>/remover/',PostDeleteView.as_view(),name='delete_post'),
    path('noticia/<int:pk>/comentarios/',views.cria_comentario,name='cria_comentario'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),

]