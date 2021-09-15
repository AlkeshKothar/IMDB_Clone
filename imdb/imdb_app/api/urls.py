
from django.urls import path, include
from imdb_app.api.views import StreamPlatfromAV , WatchDetailAV, WatchListAV , StreamPlatfromDetailAV

urlpatterns = [
    path('list',WatchListAV.as_view(), name="movie-list"),
    path('<int:pk>',WatchDetailAV.as_view(), name="movie-detail"),
    path('stream/',StreamPlatfromAV.as_view(), name="stream-list"),
    path('stream/<int:pk>',StreamPlatfromDetailAV.as_view(), name="stream-detail"),
]