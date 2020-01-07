from django.shortcuts import render
# from .models import Patient, Visit
from django.views import View
from .models import Patient, Visit


class PatientView(View):

    def get(self, request):
        patients = Patient.objects.order_by('last_name')
        ctx = {
            'patients': patients,
        }
        return render(request, "Pt_list.html", ctx)

class VisitView(View):

    def get(self, request):
        visits = Visit.objects.order_by('date_visit')
        ctx = {
            'visits': visits,
        }
        return render(request, "Visit_list.html", ctx)

