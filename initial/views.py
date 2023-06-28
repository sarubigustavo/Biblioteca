from django.shortcuts import render, redirect
#from django.http import HttpResponse
from initial.forms import CreateBookForm, FindBookForm
from initial.models import Book

# Create your views here.

def initial(request):
    return render(request, 'initial/initial.html')

def createBook(request):
    #msgLabel = ''
    if request.method == 'POST':
        formBook = CreateBookForm(request.POST)
        if formBook.is_valid():
            infoBook = formBook.cleaned_data
            book = Book(isbn=infoBook['isbn'], title=infoBook['title'], author=infoBook['author'], edition=infoBook['edition'])
            book.save()
            #msgLabel =  f'Book "{book.title}" has been created.'
            return redirect('initial:book_list')
        else:
            return render(request, 'initial/create_book.html', {'formBook': formBook})
        
    formBook = CreateBookForm()
    return render(request, 'initial/create_book.html', {'formBook': formBook})
    #return render(request, 'initial/create_book.html', {'formBook': formBook, 'msgLabel': msgLabel})
    
def listBook(request):
    formBook = FindBookForm(request.GET)
    if formBook.is_valid():
        titleBook = formBook.cleaned_data['title']
        listBook = Book.objects.filter(title__icontains=titleBook)

    formBook = FindBookForm()
    return render(request, 'initial/list_book.html', {'formBook': formBook, 'listBook': listBook})
    