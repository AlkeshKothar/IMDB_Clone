
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from imdb_app.models import WatchList, StreamPlatfrom, Review
from imdb_app.api.serializers import WatchListSerializer , StreamPlatfromSerializer , ReviewSerializer



class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=movie)

class ReviewDetail(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter (watchlist = pk)

class ReviewList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

#mixins 
'''
class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
'''






class StreamPlatfromAV(APIView):

    def get(self, request):
        platform = StreamPlatfrom.objects.all()
        serializer =  StreamPlatfromSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =  StreamPlatfromSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):

    def get(self, request,pk):
        movies = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movies)
        return Response(serializer.data)


class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatfromDetailAV(APIView):

    def get(self, request,pk):
        try:
            platform = StreamPlatfrom.objects.get(pk = pk)
        except StreamPlatfrom.DoesNotExist:
            return Response ({'error' : 'Not Found'}, status= status.HTTP_404_NOT_FOUND)
        serializer =  StreamPlatfromSerializer(platform)
        return Response(serializer.data)


    def put(self, request, pk):
        platform = StreamPlatfrom.objects.get(pk = pk)
        serializer =  StreamPlatfromSerializer(platform,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        platform = StreamPlatfrom.objects.get(pk = pk)
        platform.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)











'''
class StreamPlatfromAV(APIView):

    def get(self, request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request,pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

'''




#function based views 
'''
@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data) 
    
    if request.method == "POST":
        serializer = MovieSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request,pk):
    if request.method == "GET":
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data) 
    

    if request.method == "PUT":
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    
    if request.method == "DELETE":
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)'''