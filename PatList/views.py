from django.shortcuts import render
# from .models import Patient, Visit
from django.urls import reverse_lazy
from django.views import View
from .models import Patient, Visit
from django.views.generic import CreateView,  FormView, ListView



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

class PatientVisitView(View):
        def get(self, request, patient_id):
            visits = Visit.objects.filter(patient = patient_id)
            patient = Patient.objects.get(pk=patient_id)
            ctx = {
                'visits': visits,
                'patient': patient,
            }
            return render(request, "Patient_Visit_list.html", ctx)


class AddPatientCreateView(CreateView):
    model = Patient
    fields = "__all__"
        # ['first_name','last_name']
    template_name = 'add_patient.html'
    success_url = reverse_lazy('patients')
