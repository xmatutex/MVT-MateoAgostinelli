from mailbox import NoSuchMailboxError
from pipes import Template
from django.http import HttpResponse
from django.template import Context, Template, render


def inicio (request):
    return render(request, "Appfamilia/inicio.html")

def familia (request):
    return render(request, "Appfamilia/familiares")

