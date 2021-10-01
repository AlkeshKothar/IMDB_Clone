
from django.urls import path, include
from imdb_app.api.views import StreamPlatfromAV , WatchDetailAV, WatchListAV , StreamPlatfromDetailAV, ReviewList , ReviewDetail,ReviewCreate

urlpatterns = [
    path('list',WatchListAV.as_view(), name="movie-list"),
    path('<int:pk>',WatchDetailAV.as_view(), name="movie-detail"),
    path('stream/',StreamPlatfromAV.as_view(), name="stream-list"),

    path('stream/<int:pk>',StreamPlatfromDetailAV.as_view(), name="stream-detail"),

    path('<int:pk>/review-create',ReviewCreate.as_view(), name="review-create"),
    path('<int:pk>/review',ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>',ReviewDetail.as_view(), name="review-detail"),
]