from django.urls import path
from.import views
urlpatterns = [
    path("",views.index,name = "index"),
    path("annapurna/",views.annapurna,name="annapurna"),
    path("Exam Seater/",views.esa,name= "Exam Seater"),
    path("Jaipothyexim/",views.jai,name = "Jaipothyexim"),
    path('resume/',views.resume,name = 'resume'),
    path('contact/',views.contact,name = 'contact'),
    path('mail/',views.mail,name = 'mail'),
]
