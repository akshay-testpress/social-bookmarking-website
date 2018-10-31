from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, forms
# from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


def signup(request):
    # if request.user.is_authenticated():
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('users:home')

    else:  # get
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})

# for testing purpose

# @login_required(login_url="users:login")
# def home(request):
#     username = request.user.get_username()
#     # html = "<html><body>Logged in . welcome "+username+"</body></html>"
#     # return HttpResponse(html)

#     # return render(request,'users/home.html')

#     return redirect('musics:songlist')


def loginView(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('musics:songlist')
    else:
        form = forms.AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Log out user and redirect to login page


def logOut(request):
    logout(request)
    return redirect('users:login')
