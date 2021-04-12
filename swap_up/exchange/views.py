from django.shortcuts import render
# from django.template import loader
from django.views.generic import View
from django.views import generic
from django.utils import timezone
import io
import csv
from django.http import HttpResponseRedirect

from .forms import AddExchangeForm, UploadFileForm


from django.shortcuts import render
  
  



class IndexView(generic.TemplateView):
    template_name = 'exchange/index.html'

def home(request):
    return render(request, 'exchange/index.html')



def import_schedule(csv_file, user):
    
    classes = []
    student = Student.objects.get(user = user)
   
    reader = csv.reader(csv_file, delimiter = ';', quotechar = '|')
    for row in reader:

        io_string = io.StringIO(data)
        # next(io_string)
        for column in csv.reader(io_string, delimiter = ',', quotechar = "|"):
            try:
                subject_name = column[0] 
                term_type = column[1]
                term_capacity = column[2]
                group_number = column[3]
                teacher_name = column[4]
                room = column[5]
                # TODO: zajecia co tydzien nie maja tej kolumny, sprawdzac liczbe kolumn
                week = column[6] 
                day = column[7]
                hour = column[8]
            except:
                pass

        subject = Subject.objects.get(subject_name = subject_name)
        teacher_first_name, teacher_last_name = teacher_name.split()
        teacher = Teacher.objects.get(first_name = teacher_first_name, last_name = teacher_last_name)

        created_class = Class.objects.create(
            subject_id = subject,
            day = day,
            time = time,
            row = row,
            teacher_id = teacher
        )

        classes.append(created_class)


def upload_csv(request):
    #if request.user
    if request.method == 'POST' and request.FILES['myfile']:

        myfile = request.FILES['myfile']
        for line in myfile:
            print(line)

        import_schedule(request.FILES['myfile'], request.user)

        return render(request, 'exchange/upload_csv.html')

    return render(request, 'exchange/upload_csv.html')



def register():
    return render(request, 'exchange/index.html')

def login():
    return render(request, 'exchange/index.html')

def offers(request):
    return render(request, 'exchange/offers.html')

def manage(request):
    return render(request, 'exchange/manage.html', {'exchanges': ["Semestr 1","Semestr 2","Semestr 3","Semestr 4","Semestr 5"]})

def add_exchange(request):
    return render(request, 'exchange/add_exchange.html')

def add_offer(request):
  

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        form = AddExchangeForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data.get("subject_name"))

            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddExchangeForm()

    context = {
        'form':form
    }


    return render(request, 'exchange/add_offer.html', context)

def edit_exchange(request):
    return render(request, 'exchange/edit_exchange.html')

def user_offers(request):
    #TODO Te słowniki można by tworzyć w tym miesjcu na podstawie bazy
    # I podawać poprawne zamiast tych przykładowych

    offer1 = {
        "subject": "Teoria nicości2",
        "have_time": "Pn A, 8:00",
        "have_teacher": "Zenon Iksiński",
        "state" : "new", #Można zmienić nazwy stanów z new, pending i closed, to tylko moja propozycja
        "other_student": None,
        "other_time": None,
        "other_teacher": None
    }

    offer2 = {
        "subject": "Teoria nicości",
        "have_time": "Pn A, 8:00",
        "have_teacher": "Zenon Iksiński",
        "state" : "pending", #Można zmienić nazwy stanów z new, pending i closed, to tylko moja propozycja
        "other_student": "Staszek Ciaptak-Gąsiennica",
        "other_time": "Wt B, 9:35",
        "other_teacher": None
    }

    offer3 = {
        "subject": "Wprowadzenie do teorii nicości",
        "have_time": "Pn A, 8:00",
        "have_teacher": "Zenon Iksiński",
        "state" : "closed", #Można zmienić nazwy stanów z new, pending i closed, to tylko moja propozycja
        "other_student": "Józio Chmura-Mamałyga",
        "other_time": "Wt B, 9:35",
        "other_teacher": None
    }


    offers = [offer1, offer2, offer3]
    return render(request, 'exchange/user_offers.html', {'offers': offers})


def schedule(request):
    #Todo

    Pn = [
        {'start': 8.00, 'end': 9.35, 'subject': "Analiza", 'week':None, 'teacher':"Zenon Iksiński"},
        {'start': 9.35, 'end': 11.15, 'subject': "Analiza", 'week':None, 'teacher':"Zenon Iksiński"},
        {'start': 14.40, 'end': 16.10, 'subject': "Analiza", 'week':None, 'teacher':"Zenon Iksiński"},
    ]
    return render(request, 'exchange/shedule.html', {'Pn':pn, 'Wt':wt, 'Śr':sr, 'Czw':czw, 'Pt':pt, 'Sb':sb, 'Nd':nd})