from django.shortcuts import render, redirect
from .models import Movie
from .views import View
from .forms import MovieForm

def all_movies(request):
    movies = Movie.objects.all()
    return render(request, '', {'movies': movies})

class MovieDetail(View):
    def get(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        return render(request, '', {'movie': movie})
    
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_movies')
    else:
        form = MovieForm()
    return render(request, '', {'form': form})