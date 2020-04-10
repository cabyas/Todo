from django.shortcuts import render
from django.views import View


# function based view
def hello_page(request):
    if request.method == 'GET':
        return render(request, 'hello.html')


# class based view
class HelloView(View):
    
    def get(self, request):
        return render(request, 'hello.html')

