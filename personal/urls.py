from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.index_view, name='index'),
    path('cv/', views.cv_view, name='cv'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<int:post_id>/', views.post_detail, name='post_detail'),

    path('polls/', views.polls_list, name='polls_list'),
    path('polls/<int:question_id>/', views.poll_detail, name='polls_detail'),  
    path('polls/<int:question_id>/vote/', views.vote, name='polls_vote'),
    path('polls/<int:question_id>/results/', views.poll_results, name='polls_result'),  
]