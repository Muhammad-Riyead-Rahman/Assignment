from django.shortcuts import render, redirect  

from employee.forms import EmployeeForm  
from employee.models import Employee  


# Create your views here.


# Entry the form value here  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm() 
         
    return render(request,'index.html',{'form':form})  


# Show the existing form value here
def show(request):  
    employees = Employee.objects.all()  
    
    return render(request,"show.html",{'employees':employees}) 


# Display Edit Form With existing value 
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    
    return render(request,'edit.html', {'employee':employee})  


# Update the form with override value
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    
    if form.is_valid():  
        form.save()  
        return redirect("/show")
      
    return render(request, 'edit.html', {'employee': employee})  


def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    
    return redirect("/show")  