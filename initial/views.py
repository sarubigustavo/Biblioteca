from django.shortcuts import render
#from django.http import HttpResponse
from initial.forms import CreateBookForm
from initial.models import Book

# Create your views here.

def initial(request):
    return render(request, 'initial/initial.html')

def createBook(request):
    msgLabel = ''
    if request.method == 'POST':
        formBook = CreateBookForm(request.POST)
        #print("form content:")
        #print (formBook)
        if formBook.is_valid():
            infoBook = formBook.cleaned_data
            #print("dicc form")
            #print(infoBook)
            book = Book(isbn=infoBook['isbn'], title=infoBook['title'], author=infoBook['author'], edition=infoBook['edition'])
            book.save()
            msgLabel =  f'Book "{book.title}" has been created.'
        else:
            return render(request, 'initial/create_book.html', {'formBook': formBook})
        
    formBook = CreateBookForm()
    return render(request, 'initial/create_book.html', {'formBook': formBook, 'msgLabel': msgLabel})
    #return render(request, 'initial/create_book.html', {'formBook': formBook})