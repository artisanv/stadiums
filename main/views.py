from django.shortcuts import render
from forms import CustomUserCreationForm, CustomUserLoginForm, EditProfileForm, CreateGameForm, EditGameForm, CreateGameResultForm, EditGameResultForm
from main.models import CustomUser, Game, Game_result
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate ,login , logout
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.





    ###########################################################
    ######################## USER VIEWS #######################
    ###########################################################

def sign_up(request):

    context ={}

    context['form'] = CustomUserCreationForm()
    if request.method == 'POST' :
        form =CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email =form.cleaned_data.get('email',None)
            password = form.cleaned_data.get('password1',None)

            auth_user =authenticate(username=email, password=password)

            try:
                login(request,auth_user)
            except Exception, e :
                print e
                return HttpResponse('invalid user , try again <a href ="/signup/"> here</a>')

    return render(request,'signup.html',context)


def signin_view(request):
    context ={}

    context['form'] = CustomUserLoginForm()

    if request.method =='POST':
        form = CustomUserLoginForm(request.POST)

        if form.is_valid():
            email= form.cleaned_data.get('email',None)
            password = form.cleaned_data.get('password',None)

            auth_user = authenticate(username=email,password=password)


            try:
                login(request,auth_user)
                return render(request,'profile_page.html',context)
            except Exception , e:
                message ="""
                username or password icorrect, try again
                <a href='/signin/'> login</a>
                """
                return HttpResponse(message)

    return render(request,'signin.html',context)



def profile_page(request):
    print request.GET
    print request.POST

    context ={}

    try:
        print request.user.pk
        custom_user = CustomUser.objects.get(pk=request.user.pk)
        context['user'] = custom_user
        context['games']= custom_user.game_set.all()
    except Exception ,e:
        print e
        raise Http404('404')

    print request.user.pk

    user = CustomUser.objects.get(pk=request.user.pk)

    #return HttpResponse(user)
    return render(request,'profile_page.html',context)


def logout_view(request):
    logout(request)

    return redirect('/')



def edit_profile(request):
	context ={}



	try:
		user = CustomUser.objects.get(pk=request.user.pk)
	except Exception ,e:
		raise Http404('404')

	#context['form']=EditProfileForm(instance=user)

	form =EditProfileForm(request.POST or None, instance=user)

	context['form']=form

	if form.is_valid():
		form.save()
		return redirect('/profile_page/')
	else: print form.errors


	return render(request,'edit_profile.html',context)


    ###########################################################
    ######################## GAME VIEWS #######################
    ###########################################################

@staff_member_required
def create_game(request):
    context ={}

    form = CreateGameForm()

    context['form'] = form

    if request.method =='POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
        context['form']=form
    return render (request,'create_game.html',context)


@staff_member_required
def edit_game(request,pk):

    context= {}
    game = Game.objects.get(pk=pk)
    context['game']= game

    form = EditGameForm(request.POST or non ,instance = game)
    context['form'] = form

    if form.is_valid():
        form.save()
    redirect ('/game_detail/%s' % game.pk)


@staff_member_required
def delete_game(request,pk):
    game = Game.objects.get(pk=pk)
    game.delete()
    redirect('/game_list/')



def game_list(request):

    context ={}
    games = Game.objects.all()
    context['games']= games

    return render (request,'game_list.html',context)



def game_detail(request,pk):

    context= {}
    game = Game.objects.get(pk=pk)

    context['game']= game
    print str(game.title)

    return render(request,'game_detail.html',context)



    ###########################################################
    ######################## GAME result VIEWS #######################
    ###########################################################

@staff_member_required
def create_game_result(request, pk):
    
    context = {}

    form = CreateGameResultForm()

    context['form'] = form

    if request.method == 'POST':
        form = CreateGameResultForm(request.POST)

        if form.is_valid():
            result = form.save(commit=False)
            result.game = Game.objects.get(pk=pk)
            result.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request,'create_game_result.html', context)



@staff_member_required
def edit_game_result(request,pk):

    context= {}
    game_result = Game_result.objects.get(pk=pk)
    context['game_result']= game_result

    form = EditGameResultForm(request.POST or non ,instance = game_result)
    context['form'] = form

    if form.is_valid():
        form.save()
    redirect ('/game_detail/%s' % game.pk)



@staff_member_required
def delete_game_result(request,pk):
    game_result = Game_result.objects.get(pk=pk)
    game_result.delete()
    redirect('/game_list/')

