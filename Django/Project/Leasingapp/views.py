from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import uploadfile, register, user, adder

# Create your views here.
def frontpage(request):
    return render(request, 'Front.html')

def aboutpage(request):
    return render(request, 'About.html')

def helppage(request):
    return render(request, 'Help.html')
def contactpage(request):
    return render(request, 'Contact.html')

def reglessee(request):
    if request.method == 'POST':
        name = request.POST.get('lesname')
        username = request.POST.get('lesusername')
        password = request.POST.get('lespassword')
        address = request.POST.get('lesaddress')
        les = user()
        les.Name = name
        les.Username = username
        les.Password = password
        les.Address = address
        les.save()
        return redirect('/Front')
    return render(request, 'Lesse.html')

def reglessor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        lor = adder()
        lor.Name = name
        lor.Username = username
        lor.Password = password
        lor.Address = address
        lor.save()
        return redirect('/Front')
    return render(request, 'Lessor.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('adusername')
        password = request.POST.get('adpassword')
        if username == 'admin' and password == 'admin@123':
            return redirect('/admin')
        else:

            username = request.POST.get('adusername')
            password = request.POST.get('adpassword')

            try:
                user.objects.get(Username=username, Password=password)
                return redirect('/View')

            except:
                adder.objects.get(Username=username, Password=password)
                return redirect('/lessorview')

    return render(request, 'Front.html')

def call(request):
    return render(request, 'Admin.html')

def admin(request):
    return render(request, 'Admin.html')

def lessorview(request):
    return render(request, 'LessorView.html')

def result(request):
    details = user.objects.filter(Status=False)
    return render(request, 'PenLessee.html', {'values': details})

def result1(request):
    get = adder.objects.filter(Status=False)
    return render(request, 'PenLessor.html', {'values': get})

def approve(request, id):
    data = user.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/approved')

def approve1(request, id):
    get = adder.objects.get(id=id)
    get.Status = True
    get.save()
    return redirect('/approvedlessor')

def approved(request):
    details = user.objects.filter(Status=True)
    return render(request, 'Approved.html', {'values': details})

def approved1(request):
    deta = adder.objects.filter(Status=True)
    return render(request, 'LessorApproved.html', {'values': deta})

def lessorreg(request):

    return render(request, 'Lessor.html')

def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('des')
        price = request.POST.get('price')
        image = request.FILES['picture']
        file = uploadfile()
        file.Name = name
        file.Description = description
        file.Price = price
        file.Picture = image
        file.save()
        return redirect('/lessorview')
    return render(request, 'Add.html')

def addpen(request):
    details = uploadfile.objects.filter(Status=False)
    return render(request, 'AddPending.html', {'values': details})

def addapprove(request, id):
    data = uploadfile.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/addapproved')

def addapproved(request):
    details = uploadfile.objects.filter(Status=True)
    return render(request, 'AddApproved.html', {'values': details})

def imageview(request):
    details = uploadfile.objects.filter(Status=True)

    return render(request, 'ImageView.html', {'value': details})

def lesseregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('dev')
        days = request.POST.get('days')
        mobile = request.POST.get('number')
        email = request.POST.get('mail')
        aadhar = request.POST.get('aadhar')
        reg = register()
        reg.Name = name
        reg.Address = address
        reg.Days = days
        reg.Mobile = mobile
        reg.Email = email
        reg.Aadhar = aadhar
        reg.save()
        return redirect('/Front')
    return render(request, 'Register.html')

def regpen(request):
    details = register.objects.filter(Status=False)
    return render(request, 'PenRegister.html', {'values': details})

def regapprove(request, id):
    data = register.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/regapproved')

def approvedreg(request):
    details = register.objects.filter(Status=True)
    return render(request, 'RegApproved.html', {'values': details})

def operations(request):
    details = uploadfile.objects.all()
    return render(request, 'Edit.html',{'value': details})

def edit(request, id, status):
    details = uploadfile.objects.all()
    users = uploadfile.objects.get(id=id)
    status = uploadfile.objects.get(Status=status)
    if status == True:
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('desc')
            price = request.POST.get('price')
            image = request.FILES['picture']
            users.Name = name
            users.Description = description
            users.Price = price
            users.Image = image
            users.save()
            return redirect('/Operation')
    return render(request, 'Edit.html', {'value': details, 'a': users})

def delete(request, id):
    data = uploadfile.objects.filter(id=id).delete()
    return redirect('/delete')



