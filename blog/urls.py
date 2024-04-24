from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import NewsViewSet, LikeNews, CommentsList

router = DefaultRouter()
router.register('news', NewsViewSet, basename='news')

urlpatterns = [
    path("", include(router.urls)),
    path("like/<str:slug>/", LikeNews.as_view(), name="like"),
    path("comments/<int:id>/", CommentsList.as_view(), name="comments"),
]