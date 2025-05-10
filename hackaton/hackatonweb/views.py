from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from models import UsersModel
from hackatonweb.forms import RegisterForm

register_templates_dict = {
    "user": "...",
    "creator": "..."
}

def index(request):
    return HttpResponse("Hello, World!")


def authorized(request, id):



def register(request, type):
    return redirect(register_templates_dict.get(type))


def login(request):
    obj = RegisterForm(request.POST)
    query = get_object_or_404(UsersModel, login=obj.login)
    if query:
        redirect("index")
