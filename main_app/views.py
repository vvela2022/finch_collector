from django.shortcuts import redirect
# from django.shortcuts import render
from django.views import View #view class to handle requests
from django.http import HttpResponse #a class to handle sending a type of response
from django.views.generic.base import TemplateView 
from .models import Birds, Habitat, Zoo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
# creating a class called Home and extending it from the view class
class Home(TemplateView):
    #Here we are adding a method that will be run when we are dealing w/ a GET request
    # def get(self, request):
    #     return HttpResponse('Spotify Home')
    template_name = 'home.html' #when we use a template view, we don't have to define a get method. Django handles this for us in the background!
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zoos'] = Zoo.objects.all()
        return context

class About(TemplateView):
    template_name = 'about.html'
    # def get(self, request):
    #     return HttpResponse('Finch Collector About')



 #adds artist class for mock database data
# class BirdsList:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio


# birds = [
#   BirdsList("Gorillaz", "https://i.scdn.co/image/ab67616d00001e0295cf976d9ab7320469a00a29",
#           "Gorillaz are once again disrupting the paradigm and breaking convention in their round the back door fashion with Song Machine, the newest concept from one of the most inventive bands around."),
#   BirdsList("Panic! At The Disco",
#           "https://i.scdn.co/image/58518a04cdd1f20a24cf0545838f3a7b775f8080", "Welcome ???? The Amazing Beebo was working on a new bio but now he's too busy taking over the world."),
#   BirdsList("Joji", "https://i.scdn.co/image/7bc3bb57c6977b18d8afe7d02adaeed4c31810df",
#           "Joji is one of the most enthralling artists of the digital age. New album Nectar arrives as an eagerly anticipated follow-up to Joji's RIAA Gold-certified first full-length album BALLADS 1, which topped the Billboard R&B / Hip-Hop Charts and has amassed 3.6B+ streams to date."),
#   BirdsList("Metallica",
#           "https://i.scdn.co/image/ab67706c0000da84eb6bb372a485d26fd32d1922", "Metallica formed in 1981 by drummer Lars Ulrich and guitarist and vocalist James Hetfield and has become one of the most influential and commercially successful rock bands in history, having sold 110 million albums worldwide while playing to millions of fans on literally all seven continents."),
#   BirdsList("Bad Bunny",
#           "https://www.clashmusic.com/sites/default/files/sty???e/Bad-Bunny-YHLQMDLG-Album-2020.jpg?itok=tbZNj82L", "Benito Antonio Mart??nez Ocasio, known by his stage name Bad Bunny, is a Puerto Rican rapper, singer, and songwriter. His music is often defined as Latin trap and reggaeton, but he has incorporated various other genres into his music, including rock, bachata, and soul"),
#   BirdsList("Kaskade",
#           "https://i1.sndcdn.com/artworks-sNjd3toBZYCG-0-t500x500.jpg", "Ryan Gary Raddon, better known by his stage name Kaskade, is an American DJ, record producer, and remixer."),
# ]

@method_decorator(login_required, name='dispatch')
class BirdsList(TemplateView):
    template_name = "birds_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to access it in the request.GET dictionary object 
        name = self.request.GET.get('name')
        # if a query exists we will filter it by name
        if name != None:
            context['birds'] = Birds.objects.filter(name__icontains = name, user=self.request.user)
            # We add a header context that includes the search param
            context['header'] = f"Searching for {name}"
        else:
            context["birds"] = Birds.objects.filter(user=self.request.user) # this is where we add the key into our context object for the view to use
            # default header for not searching
            context['header'] = 'Popular Birds'
        return context

class BirdsCreate(CreateView):
    model = Birds
    fields = ['name', 'img', 'bio', 'verified_bird']
    template_name = 'birds_create.html'
    # this is our new method that will add the user into our submitted form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BirdsCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('birds_detail', kwargs={'pk': self.object.pk})


class BirdsDetail(DetailView):
    model = Birds
    template_name = 'birds_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zoos'] = Zoo.objects.all()
        return context

class BirdsUpdate(UpdateView):
    model = Birds
    fields = ['name', 'img', 'bio', 'verified_bird']
    template_name = 'birds_update.html'
    
    def get_success_url(self):
        return reverse('birds_detail', kwargs={'pk': self.object.pk})

class BirdsDelete(DeleteView):
    model = Birds
    template_name = 'birds_delete_confirmation.html'
    success_url = '/birds/'

class HabitatCreate(View):
    def post(self, request, pk):
        name = request.POST.get('name') 
        location = request.POST.get('location')
        bird = Birds.objects.get(pk=pk)
        Habitat.objects.create(name=name, location=location, birds=bird)
        return redirect('birds_detail', pk=pk)


class ZooBirdsAssoc(View):
    
    def get(self, request, pk, birds_pk):
        #get the query param from the url
        assoc = request.GET.get('assoc')
        if assoc == 'remove':
            # get the playlist by the id and 
            # remove from the join table the given song_id
            Zoo.objects.get(pk=pk).birds.remove(birds_pk)
        if assoc == 'add':
            # get the playlist by the id and
            # add to the join table the given bird_id
            Zoo.objects.get(pk=pk).birds.add(birds_pk)
        return redirect('home')

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)
    # on form submmit, validate the form and login the user
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('birds_list')
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)
