from django.contrib import admin
from imdb_app.models import StreamPlatfrom, WatchList, Review
# Register your models here.

admin.site.register(StreamPlatfrom)
admin.site.register(WatchList)
admin.site.register(Review)