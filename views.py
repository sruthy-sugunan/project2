from django.contrib.auth.models import User
from .models import Expense
from .models import Balance
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from expense_tracker.settings import EMAIL_HOST_USER

# Create your views here.
@login_required
def homee(request):
    return render(request,'exphome.html')


	

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('homee')
    else:
        return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect('login')





def sign_up(request):
        form = UserCreationForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('uname')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password)
                return redirect('homee')

                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                     return render(request,"registration/sign_up.html")



        else:
            form = UserCreationForm()
        return render(request, 'registration/sign_up.html', {'form': form})
        
                   
         
        


def Resethome(request):
    return render(request,'registration/ResetPassword.html')

def resetPassword(request):
    responseDic={}
    try:
        username = request.POST['uname']
        recepient=request.POST['email']
        pwd=request.POST['password']
        subject="Password reset"
        try:
            user=User.objects.get(username=username)
            if user is not None:
                user.set_password(pwd)
                user.save()
                message="Your password was changed"
                send_mail(subject,message, EMAIL_HOST_USER, [recepient])
                responseDic["errmsg"]="Password Reset Successfully"
                return render(request,"registration/ResetPassword.html",responseDic)
        except Exception as e:
            print(e)
            responseDic["errmsg"]="Email doesnt exist"
            return render(request,"registration/ResetPassword.html",responseDic)
        
    except Exception as e:
        print(e)
        responseDic["errmsg"]="Failed to reset password"
        return render(request,"registration/ResetPassword.html",responseDic)


def home(request):
    return render(request,'exphome.html')

def add(request):
    return render(request,'add.html')

def addexp(request):
    try:
      name=request.POST['ename']
      am=int(request.POST['amnt'])
      bal=Balance.objects.get(id=1)
      if(am>bal.balance):
        return render(request,"add.html",{"msg":"Insuffient Balance"})
      else:
          bal.balance-=am
          bal.save()
          print(bal.balance)

          con=Expense.objects.get(expense=name)
          if con is not None:
              con.amount+=am
              Expense.objects.filter(expense=name).update(amount=con.amount)
              return render(request,"add.html",{"msg":"Updated,Current balance is:"+str(bal.balance)})
    except Exception as e:
        print(e)
        alist=Expense(expense=name,amount=am)
        alist.save()
        return render(request,"add.html",{"msg":"Added,Current balance is:"+str(bal.balance)})






      




                

   
    



def update(request):
    return render(request,'addbalance.html')


def updateb(request):
    bl=int(request.POST['amnt'])
    bal=Balance.objects.get(id=1)
    bal.balance+=bl
    bal.save()
    return render(request,'addbalance.html',{'msg':"Balance Updated successfully:"+str(bal.balance)})
    



def viewex(request):
    explist=Expense.objects.all()
    return render(request,'view.html',{'det':explist})


def delete(request):
    return render(request,'delete.html')


def deleteexp(request):
    try:
      nam=request.POST['name']
      exlist=Expense.objects.get(expense=nam)
      if exlist is not None:
        expdtl=Expense.objects.filter(expense=nam)
        expdtl.delete()
        return render(request,"delete.html",{"msg":"Deleted successfully!"})

    except Exception as e:
        print(e)
        return render(request,"delete.html",{"msg":"Item not in list"})











          
    






