from django.shortcuts import render, redirect, get_object_or_404
from ksm_app.forms import (DebatantsProfileInfo, JudgesProfileInfo, UserForm,
                           JudgesForm, DebatantsBattleForm,
                           TransmisionBattle, JudgesPassword,
                           DebatantsForm, )
from ksm_app.models import Debatants, Judges, DebatantsBattle, PasswordJudges
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from ksm_app.decorators import allowed_users, unauthenticated_user
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import template
from django.utils.translation import gettext as _


# Create your views here.
def index(request):
    return render(request, 'ksm_app/index.html')


def base(request):
    return render(request, 'ksm_app/main.html')


def phone(request):
    return render(request, 'ksm_app2/phone.html')


def instruction(request):
    return render(request, 'ksm_app/instruction.html')


def about(request):
    return render(request, 'ksm_app2/about.html')
    # Register #


def ChooseRegister(request):
    return render(request, 'ksm_app2/choose_register.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('ksm_app:base')


def Login(request):
    return render(request, 'ksm_app2/login.html')


def DebatantsRegister(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        debatants_form = DebatantsProfileInfo(data=request.POST)

        if user_form.is_valid() and debatants_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            debatants = debatants_form.save(commit=False)
            debatants.user = user
            debatants.save()
            registered = True
        else:
            print(user_form.errors, debatants_form.errors)

    else:

        user_form = UserForm()
        debatants_form = DebatantsProfileInfo()

    return render(request, 'ksm_app2/register_debatant.html',
                  {'user_form': user_form,
                   'debatants_form': debatants_form,
                   'registered': registered})


def JudgesRegister(request):
    my_group = Group.objects.get(name='judges')
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        judges_form = JudgesProfileInfo(data=request.POST)

        if user_form.is_valid() and judges_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            my_group.user_set.add(user)
            judges = judges_form.save(commit=False)
            judges.user = user
            judges.save()
            registered = True
        else:
            print(user_form.errors, judges_form.errors)

    else:

        user_form = UserForm()
        judges_form = JudgesProfileInfo()

    return render(request, 'ksm_app2/register_judges.html',
                  {'user_form': user_form,
                   'judges_form': judges_form,
                   'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('ksm_app:base')

            else:
                return HttpResponse("Konto nie aktywne")

        else:
            print("ktos probowal sie zalogowac ale nie udało mu sie")
            print("Username: {} i hasło {}".format(username, password))
            return HttpResponse('nie właściwe dane do logowania')

    else:
        return render(request, 'ksm_app2/login.html', {})


def judges_list(request):
    judges = Judges.objects.all()
    return render(request, 'ksm_app2/judge_list.html', {'judges': judges})


def judges_detail(request, pk):
    judges = Judges.objects.get(id=pk)
    return render(request, 'ksm_app2/judges_detail.html', {'judges': judges})


def debatants_list(request):
    debatants = Debatants.objects.all()
    return render(request, 'ksm_app2/debatants_list.html', {'debatants': debatants})


def debatants_detail(request, pk):
    debatants = Debatants.objects.get(id=pk)
    return render(request, 'ksm_app2/debatants_detail.html', {'debatants': debatants})


def live(request, m, d):
    data = _('%(month), %(day)') % {'month': m, 'day': d}
    return render(request, 'ksm_app2/live.html')

    # Battle


def ShowBattle(request):
    battles = DebatantsBattle.objects.all()
    return render(request, 'ksm_app2/live.html', {'battles': battles})


@allowed_users(allowed_roles=['judges'])
def createBattle(request):
    form = DebatantsBattleForm()

    if request.method == "POST":
        form = DebatantsBattleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ksm_app:live')

    context = {'form': form}
    return render(request, 'ksm_app/battle_form.html', context)


@allowed_users(allowed_roles=['judges'])
def updateBattle(request, pk):
    battle = DebatantsBattle.objects.get(id=pk)
    form = DebatantsBattleForm(instance=battle)

    if request.method == "POST":
        form = DebatantsBattleForm(request.POST, instance=battle)
        if form.is_valid():
            form.save()
            return redirect('ksm_app:live')

    context = {'form': form}
    return render(request, 'ksm_app/battle_form.html', context)


@allowed_users(allowed_roles=['judges'])
def deleteBattle(request, pk):
    battle = DebatantsBattle.objects.get(id=pk)
    if request.method == "POST":
        battle.delete()
        return redirect('ksm_app:live')

    context = {'item': battle}
    return render(request, 'ksm_app/delete.html', context)


def judgesAuth(request):
    model = PasswordJudges.objects.all()
    form = JudgesPassword()
    password = 'TjQWnc2D2w6'
    if request.method == 'POST':
        form = JudgesPassword(request.POST)
        if form.is_valid():
            haslo = form.cleaned_data['haslo']
            if haslo == password:
                return redirect('ksm_app:judges')
            else:
                return HttpResponse('Hasło nie prawidłowe')

    return render(request, 'ksm_app2/allowed.html', {'form': form})

    # User profile #


def debatantsProfilePage(request):
    return render(request, 'ksm_app/debatants_profile.html')


def judgesProfilePage(request):
    return render(request, 'ksm_app/judges_profile.html')


def edit_judges_profile(request):
    if request.method == "POST":
        form = JudgesForm(request.POST, instance=request.user.judges)

        if form.is_valid():
            form.save()
            return redirect('ksm_app:judges_profile')

    else:
        form = JudgesForm(instance=request.user.judges)
        context = {'form': form}
        return render(request, 'ksm_app/judges_form.html', context)


def edit_debatants_profile(request):
    if request.method == "POST":
        form = DebatantsForm(request.POST, instance=request.user.debatants)

        if form.is_valid():
            form.save()
            return redirect('ksm_app:debatants_profile')

    else:
        form = DebatantsForm(instance=request.user.debatants)
        context = {'form': form}
        return render(request, 'ksm_app/debatants_form.html', context)
