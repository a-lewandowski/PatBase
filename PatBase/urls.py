"""PatBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from PatList.views import PatientView, VisitView, AddPatientCreateView, PatientVisitView,
import PatList.views
from django.conf.urls import url

urlpatterns = {
    path('admin/', admin.site.urls),
    url(r'^$', PatList.views.PatientView.as_view(), name="patients"),
    path('visits/', PatList.views.VisitView.as_view(), name="visits"),
    url(r'^add_patient/', PatList.views.AddPatientCreateView.as_view(), name="add-patient"),
    url(r'^patvis/(?P<patient_id>(\d)+)/', PatList.views.PatientVisitView.as_view(), name="patientvisit"),
    url(r'^add_visit/', PatList.views.AddVisitCreateView.as_view(), name="add-visit"),

}
