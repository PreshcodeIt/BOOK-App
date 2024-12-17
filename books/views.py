from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from django.core.files.storage import FileSystemStorage

def list_books(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        file = request.FILES['file']
        Book.objects.create(title=title, author=author, description=description, file=file)
        return redirect('list_books')
    return render(request, 'books/add.html')

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.description = request.POST['description']
        if 'file' in request.FILES:
            book.file = request.FILES['file']
        book.save()
        return redirect('list_books')
    return render(request, 'books/update.html', {'book': book})    

def download_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    response = HttpResponse(book.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{book.file.name}"'
    return response


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'books/delete.html', {'book': book})
