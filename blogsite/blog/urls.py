from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='post_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
