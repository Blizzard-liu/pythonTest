from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Book
from django.utils import timezone
from django.urls import reverse
def index(request):
    return HttpResponse('hello world')


def detail(request):
    book_list = Book.objects.order_by('-pub_date')[:5]
    context = {'book_list':book_list}
    return render(request,'lib/detail.html',context)

def addBook(request):
    if request.method == "POST":
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']
        temp_book = Book(name = temp_name,author = temp_author,
                     pub_house = temp_pub_house,pub_date =timezone.now())
        temp_book.save()
        return HttpResponseRedirect(reverse('lib:detail'))

def delBook(request,book_id):
    bookID = book_id
    Book.objects.filter(id=bookID).delete()
    return HttpResponseRedirect(reverse('lib:detail'))