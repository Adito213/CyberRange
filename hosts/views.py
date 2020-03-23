import os

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *

from .models import *

from django.template.loader import get_template
from io import BytesIO
from django.views import View
from xhtml2pdf import pisa


def is_valid_query_param(param):
    return param != '' and param is not None


# Create your views here.

@login_required(login_url='login')  # restrict login
def home(request):
    # hosts_data = Host.objects.all()
    # for fild in hosts_data:
    #     print("First name of student is:", fild.first_name)
    #     print("Last name of student is:", fild.last_name)
    #     print("Email of student is:", fild.email)
    #     print("Team of student is:", fild.team)
    #
    # return HttpResponse("this url is working")

    return render(request, 'hosts/home.html')


@login_required(login_url="login")
def screenshots(request):
    qs = Sreenshots.objects.all()
    sources = Source.objects.all()
    teams = Team.objects.all().exclude(team="White")

    source = request.GET.get('source')
    team = request.GET.get('team')
    print(source)
    print(team)
    if is_valid_query_param(source):
        qs = qs.filter(ip_source__source=source)

    if is_valid_query_param(team):
        qs = qs.filter(team__team=team)

    context = {
        'qs': qs,
        's': sources,
        't': teams,
        # 'f' : form,
    }

    return render(request, 'hosts/screenshots.html', context)


@login_required(login_url="login")
def logs(request):
    qs = Logs.objects.all()

    ip_source = Source.objects.all()
    teams = Team.objects.all().exclude(team="White")

    source = request.GET.get("source")
    team = request.GET.get("team")

    if is_valid_query_param(source) and source != 'Choose...':
        qs = qs.filter(ip_source__source=source)
    if is_valid_query_param(team):
        qs = qs.filter(team__team=team)

    form = Description(request.POST)
    if form.is_valid():
        description = form.save(commit=False)
        description.plaintext = form.plaintext
        description.ip_source = form.ip_source
        description.category = form.category
        description.team = form.team
        description.save()

    context = {
        'qs': qs,
        's': ip_source,
        't': teams,
        'f': form,
    }
    return render(request, 'hosts/logs.html', context)


@login_required(login_url="login")
def sources(request):
    sources = Source.objects.all()
    return render(request, 'hosts/source.html', {'s': sources})


@login_required(login_url="login")
def teams(request):
    team = Team.objects.all()
    return render(request, 'hosts/team.html', {'t': team})


@login_required(login_url="login")
def category(request):
    category = Category.objects.all()
    return render(request, 'hosts/category.html', {'c': category})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'hosts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or password is incorrect")

        context = {}
        return render(request, 'hosts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def addDesc(request):
    form = Description(request.POST)
    if form.is_valid():
        description = form.save(commit=False)
        description.img = form.img
        description.ip_source = form.ip_source
        description.category = form.category
        description.team = form.team
        description.save()
    args = {'form': form, }
    return render(request, 'hosts/screenshots.html', args)


def training(request):
    topology = Trainings.objects.get(pk=1)

    return render(request, "hosts/training.html", {'t': topology})


def results(request):
    artefactsScr = Sreenshots.objects.exclude(description="").order_by('created_at')
    artefactsLog = Logs.objects.exclude(description="").order_by('created_at')

    categories = Category.objects.all()
    cat = request.GET.get('category')

    if is_valid_query_param(cat) and cat == 'Logs':
        artefactsScr = None

    if is_valid_query_param(cat) and cat == 'Screenshots':
        artefactsLog = None

    context = {
        'screen': artefactsScr,
        'log': artefactsLog,
        'cat': categories,
    }

    return render(request, "hosts/results.html", context)


def archives(request):
    return render(request, "hosts/archives.html")


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='/pdf')
    return None


class ViewPDF(View):

    def get(self, request, *args, **kwargs):
        screenshots = Sreenshots.objects.exclude(description="").order_by('created_at')
        logs = Logs.objects.exclude(description="").order_by('created_at')

        data = {
            'screenshots': screenshots,
            'logs': logs,
        }

        pdf = render_to_pdf('hosts/pdf.html', data)
        return HttpResponse(pdf, content_type='/pdf')


# Automaticly downloads to PDF file
class DownloadPDF(View):

    def get(self, request, *args, **kwargs):
        screenshots = Sreenshots.objects.exclude(description="").order_by('created_at')
        logs = Logs.objects.exclude(description="").order_by('created_at')

        data = {
            'screenshots': screenshots,
            'logs': logs,
        }

        pdf = render_to_pdf('hosts/pdf.html', data)

        response = HttpResponse(pdf, content_type='/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
