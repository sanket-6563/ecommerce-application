from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


def contact(request):
    return HttpResponse("<h1> Welcome to contact page </h1>")

def edit(request,rid):
    print("Id to be edited: ",rid)
    return HttpResponse("Id to be edited: "+rid)

def delete(request,rid):
    print("Id to be deleted: ",rid)
    return HttpResponse("Id to be deleted: "+rid)

class SimpleView(View):
    def get(self,request):
        return HttpResponse("Hello From simple view")
    
def hello(request):
    context={}
    context['greet']="Good morning"
    
    context['x']=10
    context['y']=20
    
    context['l']=[1,2,3,4,5]
    
    context['product']=[
        {'id':1,'name':'Harry','category':'phone','prize':20000},
        {'id':2,'name':'Mac','category':'Laptop','prize':100000},
        {'id':3,'name':'Shree','category':'TV','prize':50000}
    ]  
    return render(request,'hello.html',context)

def home(request):
    return render(request,'index.html')

def pdetails(request):
    return render(request,'product_details.html')

def register(request):
    if request.method=='POST':

        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        if uname=="" or upass=="" or ucpass=="":
            context={}
            context['ermsg']="field can not be empty"
            return render(request,'register.html',context)
        else:
            u=User.objects.create(username=uname,password=upass,email=uname)
            u.set_password(upass)
            u.save()
            return HttpResponse("data is fetch successfully")
    
    else:
        return render(request, 'register.html')

def login(request):
    return render(request,'login.html')