from django.shortcuts import render

# Create your views here.
def index(request):
      return render(request, "index.html")
def email(request):
      return render(request, "app-emailbox.html")
def chat(request):
      return render(request, "app-chat-box.html")
def file(request):
      return render(request, "app-file-manager.html")
def contact(request):
      return render(request, "app-contact-list.html")
def todo(request):
      return render(request, "app-to-do.html")
def invoice(request):
      return render(request, "app-invoice.html")
def calender(request):
      return render(request, "backend.html")

