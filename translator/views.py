from django.shortcuts import render, redirect
from .models import Translation
from .forms import SearchForm


def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_word = form.cleaned_data['search_word']
            translations = Translation.objects.filter(arabic_word=search_word) | Translation.objects.filter(kyrgyz_word=search_word)
            return render(request, 'translator/home.html', {'form': form, 'translations': translations})
    else:
        form = SearchForm()
    return render(request, 'translator/home.html', {'form': form})


def admin_panel(request):
    translations = Translation.objects.all()
    return render(request, 'translator/admin_panel.html', {'translations': translations})


def add_translation(request):
    if request.method == 'POST':
        arabic_word = request.POST.get('arabic_word')
        kyrgyz_word = request.POST.get('kyrgyz_word')
        meaning = request.POST.get('meaning')
        Translation.objects.create(arabic_word=arabic_word, kyrgyz_word=kyrgyz_word, meaning=meaning)
    return render(request, 'translator/add_translation.html')


def search_word(request):
    translations = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_word = form.cleaned_data['search_word']
            if request.user.is_superuser:  # Если пользователь администратор
                translations = Translation.objects.filter(arabic_word__istartswith=search_word)
            else:
                translations = Translation.objects.filter(arabic_word__startswith=search_word)
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form, 'translations': translations})

