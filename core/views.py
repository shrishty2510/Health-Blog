from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib import messages
from matplotlib import image
from matplotlib.pyplot import title
from . forms import MainUser,Extenduser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from . models import SignUp
from . forms import login_form
from blog.forms import Postform
from blog.models import Post

def homepage(request):
    return render(request,'core/base.html')

def sign_up(request):
    if request.method == 'POST':
        user = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_type = request.POST['user_type']
        image = request.FILES['profile_image']
        locality = request.POST['locality']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        if password1 != password2:
            messages.error(request,"password does not matched!")  
        elif User.objects.filter(username = user).first():
            messages.error(request, "This username is already taken")
            return HttpResponseRedirect('/')    
        else:    
            user1 = User.objects.create_user(user, email, password1)
            user1.first_name=fname
            user1.last_name=lname
            user1.save()
            user = User.objects.get(username=user)
            print(user)
            us2 = SignUp(user=user,user_type=user_type, profile_image=image, locality=locality,city=city,state=state,pin=pin)
            print(user)
            us2.save()
            messages.success(request,"signup successfully")
            return HttpResponseRedirect('/register/')
    return render(request,'core/home.html',{'form1':MainUser,'form2':Extenduser})

        
def loginform(request):
    if request.method == 'POST':
        fr = login_form(request.POST)
        if fr.is_valid():
            data=fr.cleaned_data
            uname=data['Username']
            upass=data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                User=SignUp.objects.get(user=user)
                if User.user_type == 'Doctor':
                   return HttpResponseRedirect('/profile/')
                else:
                   return HttpResponseRedirect('/userprofile/')    
            else :
                 messages.error(request, "Please check your username and password!!")
                 return redirect('/login/')

    else:        
        fr = login_form()
    return render(request,'core/login.html',{'form':fr})   



def logoutform(request):
    logout(request)
    return HttpResponseRedirect('/login/')   

def profilepage(request):
    if request.user.is_authenticated:
            us = User.objects.get(username = request.user)
            us1 = SignUp.objects.get(user= request.user)
            form=Postform()
            return render(request,'core/profile.html',{'user':us,'detail':us1,'pform':form})              
    else:        
        return redirect('/login/') 

def userprofilepage(request):
    if request.user.is_authenticated:
            us = User.objects.get(username = request.user)
            us1 = SignUp.objects.get(user= request.user)
            return render(request,'core/userprofile.html',{'user':us,'detail':us1,})              
    else:        
        return redirect('/login/')         
             
         
                 
           

        

def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=Postform(request.POST,request.FILES)
            if form.is_valid():
                dt=form.cleaned_data
                title=dt['title']
                image=dt['image']
                category=dt['category']
                content=dt['content']
                summary=dt['summary']
                postt=Post(title=title,image=image,category=category,content=content,summary=summary)
                postt.save()
                messages.success(request,'Post successfully added!!')
            return redirect('/profile/')    

        else:
            return redirect('/profile/')    
    else:        
        return  HttpResponseRedirect('/login/')
def showpost(request):
    if request.user.is_authenticated:
      post1=Post.objects.filter(category='Mental Health')
      return render(request,'blog/table.html',{'post':post1})
def showpost1(request):
    if request.user.is_authenticated:
      post1=Post.objects.filter(category='Covid-19')
      return render(request,'blog/table2.html',{'post':post1})
def showpost2(request):
    if request.user.is_authenticated:
      post1=Post.objects.filter(category='Immune System')
      return render(request,'blog/table3.html',{'post':post1})
def showpost3(request):
    if request.user.is_authenticated:
      post1=Post.objects.filter(category='Heart Disease')
      return render(request,'blog/table4.html',{'post':post1})      

def userpost(request):
    if request.user.is_authenticated:
      post1=Post.objects.filter(category='Mental Health')
      return render(request,'blog/usertable.html',{'post':post1})
def userpost1(request):
    if request.user.is_authenticated:
      post1=Post.objects.filter(category='Covid-19')
      return render(request,'blog/usertable1.html',{'post':post1})
def userpost2(request):
    if request.user.is_authenticated:
      post1=Post.objects.filter(category='Immune System')
      return render(request,'blog/usertable2.html',{'post':post1})
def userpost3(request):
    if request.user.is_authenticated:
      post1=Post.objects.filter(category='Heart Disease')
      return render(request,'blog/usertable3.html',{'post':post1})      

def delete_data(request,id):
    if request.user.is_authenticated:
            pi = Post.objects.get(pk=id)
            pi.delete()
            messages.success(request,"Deleted Successfully !!")
            return redirect('/profile/')  
    else:
        pass 

def particular(request,id):
        print(id)
        posts= Post.objects.get(id=id)
        return render(request,'blog/review.html',{'post':posts})    

              
