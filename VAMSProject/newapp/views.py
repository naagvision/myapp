from django.shortcuts import render, redirect, HttpResponse
from newapp import views
from newapp.form import EmployeeForm
from newapp.models import Employee12
from django.db.models import Q
import json
# Create your views here.


def home_view(request):

    return render(request,'newapp/home.html')

def cardholder_view(request):

    return render(request,'newapp/cardholder.html')

def Employee_info_view(request):

    return render(request,'newapp/results.html')

def create(request):
    return render(request,'newapp/show.html')

# This code create Employee data and after that it show all employee.
def emp(request):
    form = EmployeeForm
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                #if(form.checkIfRecordExist()==false):
                    form.save()
                    return redirect("/show")
                #else:
                    #message.render('Record alredy exist..!!')

            except:
                pass
        else:
            form = EmployeeForm()
    return render(request,'newapp/index.html',{'form':form})

#checkIfRecordExist



def show(request):
    employees = Employee12.objects.all()
    return render(request,'newapp/show.html',{'employees':employees})
#below code for edit employee data.
def edit(request,id):
    employee = Employee12.objects.get(id=id)
    return render(request,"newapp/edit.html",{'employee':employee})
#Below code for update and redirect show page.
def update(request,id):
    employee =Employee12.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)

    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"newapp/edit.html",{'employee12':employee})
#below code for delete id.
def delete(request,id):
    employee = Employee12.objects.get(id=id)
    employee.delete()
    return redirect("/show")
# Below code for search key.
def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Employee12.objects.filter(Q(eid__icontains=srch) | Q(efname__icontains=srch) |
            Q(elname__icontains=srch))
            if match:
                return render (request,'newapp/cardholder.html',{'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search')
    return render(request,'newapp/cardholder.html')

        #id = request.POST.get('id')
        #card = request.POST.get('card')
        #firstname = request.POST.get('firstname')
        #lastname = request.POST.get('lastname')
        #agency = request.POST.get('agency')
    #return render(request,'testapp/create_new.html')

#def results_view(request):
    #if request.method == "POST":
        #name = request.POST['card','id','firstname','lastname','agency']
        #print(name)

    #return render(request,'testapp/result.html')
import json
def emp_view_json(request):
    emp_data={
    'eno':100,
    'ename':'Almas',
    'esal':20000,
    }
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')
