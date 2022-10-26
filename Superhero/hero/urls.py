from django.urls import path, include
from django.views.generic import RedirectView
from .views import GalleryListView, HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView, SignUpView, UserUpdateView
from .views_articles import ArticleCreateView, ArticleListView, ArticleDeleteView, ArticleDetailView, ArticleUpdateView
from .views_investigators import InvestigatorCreateView, InvestigatorListView, InvestigatorDeleteView, InvestigatorDetailView, InvestigatorUpdateView
from django.contrib import admin

urlpatterns = [

    # Gallery
    path('gallery',                GalleryListView.as_view(),    name='hero_gallery'),
    # Hero
    path('',                HeroListView.as_view(),    name='hero_list'),
    path('hero',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
    #Account Views
    path('accounts/signup/', SignUpView.as_view(), name = 'signup'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #Article Views
    path('article/',                  ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>',          ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',               ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/',         ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete',   ArticleDeleteView.as_view(),  name='article_delete'),
    #Investigator View
    path('investigator/',                  InvestigatorListView.as_view(),    name='investigator_list'),
    path('investigator/<int:pk>',          InvestigatorDetailView.as_view(),  name='investigator_detail'),
    path('investigator/add',               InvestigatorCreateView.as_view(),  name='investigator_add'),
    path('investigator/<int:pk>/',         InvestigatorUpdateView.as_view(),  name='investigator_edit'),
    path('investigator/<int:pk>/delete',   InvestigatorDeleteView.as_view(),  name='investigator_delete'),
]
