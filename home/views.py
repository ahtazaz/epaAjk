from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Water,Air,Contact,blog,news
import pandas as pd
import matplotlib.pyplot as plt
from .utils import get_simple_plot
from influxdb import DataFrameClient
from django.contrib import messages
from .getair import datainput
# Create your views here.
def index(request):
    post = blog.objects.all().last()
    new = news.objects.all().last()
    return render(request, 'index.html',{'post':post ,'new':new})

def contact(request):
    c = Contact()
    if request.method=="POST":
        c.name = request.POST['fname']
        c.email = request.POST['email']
        c.message = request.POST['message']
        c.save()
        return redirect('index')
    return render(request,'contactUs.html')

@login_required
def blogs(request):
    if request.method=="POST":
        title = request.POST['title']
        discription = request.POST['discription']
        d = blog(title=title,discription=discription)
        d.save()
    return render(request,'post.html')

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request,'login.html')    
def logout_user(request):
    logout(request)
    return redirect('index')
    
def register_user(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass']
        user =User.objects.create_user(username=email,password=password)
        user.save()
        return redirect('g')
    return render(request,'register.html')
def slider(request):
    return render(request,'Water.html')


def water(request):
    chart_type=None
    graph = None
    client = DataFrameClient(host='localhost', port=8086)
    client.switch_database('NOAA_water_database')
    f=client.query("Select * from h2o_pH")
    df = pd.concat(f)
    df=df.reset_index(level=[0,1])
    #df = pd.DataFrame(Air.objects.all().values(),columns=["date", "Carbon_Monoxide", "NOx", "Ozone","Particulate_Matter","SOx"])
    #df=df.set_index('date')
    if request.method =='POST' :

        chart_type = request.POST['sales']
        date_from = request.POST['date_from']
        date_to = request.POST['date_to'] 
        df['level_1'] = df['level_1'].apply(lambda x: x.strftime('%Y-%m-%d'))  
        df2 = df.groupby('level_1', as_index = False)['pH'].agg('sum')  
        if chart_type != "":
            if date_from != "" and date_to !="" :
                df = df[(df['level_1']>date_from) & (df['level_1']< date_to)]
                df2 = df.groupby('level_1', as_index=False)['pH'].agg('sum')
                graph = get_simple_plot(chart_type, x=df2['level_1'], y=df2['pH'], data=df)
    context ={
        
        'graph': graph, 
        
        
    }           
        #print(df2)
    return render(request,'Water.html',context)
def air(request):
    chart_type=None
    graph = None
    client = DataFrameClient(host='localhost', port=8086)
    client.switch_database('NOAA_water_database')
    f=client.query("Select * from h2o_pH")
    df = pd.concat(f)
    df=df.reset_index(level=[0,1])
    #df = pd.DataFrame(Air.objects.all().values(),columns=["date", "Carbon_Monoxide", "NOx", "Ozone","Particulate_Matter","SOx"])
    #df=df.set_index('date')
    if request.method =='POST' :

        chart_type = request.POST['sales']
        date_from = request.POST['date_from']
        date_to = request.POST['date_to'] 
        df['level_1'] = df['level_1'].apply(lambda x: x.strftime('%Y-%m-%d'))  
        df2 = df.groupby('level_1', as_index = False)['pH'].agg('sum')  
        if chart_type != "":
            if date_from != "" and date_to !="" :
                df = df[(df['level_1']>date_from) & (df['level_1']< date_to)]
                df2 = df.groupby('level_1', as_index=False)['pH'].agg('sum')
                graph = get_simple_plot(chart_type, x=df2['level_1'], y=df2['pH'], data=df)
    context ={
        
        'graph': graph, 
        
        
    }           
        #print(df2)
    return render(request,'air.html',context)

@login_required
def airdata(request):
    if request.method=='POST':
        a=request.POST.get('a')
        b=request.POST.get('b')
        c=request.POST.get('c')
        d=request.POST.get('d')
        e=request.POST.get('e')
        f=request.POST.get('f')
        datainput(a,b,c,d,e,f)
    return render(request,'getair.html')

def waterdata(request):
    pass
@login_required
def newsdata(request):
    if request.method=='POST':
        a=request.POST['news']
        new=news(new=a)
        new.save()
        return redirect('index')
    return render(request,'news.html')

@login_required
def waterdata(request):
    return render(request,'getwater.html')