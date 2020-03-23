from django.template.context_processors import static
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('screenshots/', views.screenshots, name='home'),
    path('logs/', views.logs, name='home'),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('add_description/', views.addDesc, name='add_description  '),

    path('source/', views.sources, name="s"),
    path('team/', views.teams, name="s"),
    path('category/', views.category, name="s"),

    path('trainingall/', views.training, name="s"),

    path('results/', views.results, name='home'),
    path('archives/', views.archives, name='home'),
    path('training/', views.training, name='home'),

    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

]
