from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout
from . import models,forms
from datetime import datetime
import json

def home(request):
    return render(request,'home.html')

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        uid=request.POST['uid']
        pwd=request.POST['pwd']
        userdata=models.UserMaster.objects.filter(userid__exact=uid).filter(password__exact=pwd)
        if userdata:
            for dt in userdata:
                request.session['userid']=dt.userid
                request.session['usertype']=dt.usertype
                unm=models.UserProfile.objects.get(userid=dt.userid)
                request.session['username']=unm.username;
            return redirect('home')
        else:
            return HttpResponse("Invalid Credentials....");

def logouts(request):
        logout(request);
        return redirect('home'); 
        
    
class AddUserView(View):
    def get(self,request):
        myform=forms.UserMasterForm();
        return render(request,'adduser.html',{'myform':myform})
    def post(self,request):
        myform=forms.UserMasterForm(request.POST)
        if myform.is_valid():
            myform.save();
        return redirect('home')

class ProfileView(View):
    def get(self,request):
        myform=forms.UserProfileForm();
        return render(request,'profile.html',{'myform':myform})
    def post(self,request):
        myform=forms.UserProfileForm(request.POST)
        if myform.is_valid():
            unm=myform.cleaned_data['username']
            age=myform.cleaned_data['age']
            add=myform.cleaned_data['address']
            mob=myform.cleaned_data['mob']
            email=myform.cleaned_data['email']
            uid=request.session['userid']
            pr=models.UserProfile(unm,age,add,mob,email,uid)
            pr.save();
            return redirect('home')

class ShowUsers(View):
    def get(self,request):
        userdata=models.UserMaster.objects.exclude(usertype__exact='admin')
        #print("User list is : ",userdata)
        return render(request,'showuser.html',{'mydata':userdata})
    
class UserDetailsView(View):
    def get(self,request,id):
        mydata=models.UserMaster.objects.get(userid__exact=id)
        return render(request,'singleuser.html',{'mydata':mydata})
    def post(self,request,id):
        obj=get_object_or_404(models.UserMaster,userid=id)
        obj.delete();
        return redirect('showuser')
    
class ProductCatView(View):
    def get(self,request):
        myform=forms.ProductCategoryForm();
        return render(request,'addprocat.html',{'myform':myform})
    def post(self,request):
        myform=forms.ProductCategoryForm(request.POST)
        if myform.is_valid():
            myform.save();
        return redirect('home')
    
def showProCat(request):
    data=models.ProductCategory.objects.all();
    return render(request,'showprocat.html',{'mydata':data})

class UpdateProCat(View):
    def get(self,request,id):
        obj=get_object_or_404(models.ProductCategory,pcid=id)
        myform=forms.ProductCategoryForm(instance=obj)
        return render(request,'updprocat.html',{'myform':myform})
    def post(self,request,id):
        obj=get_object_or_404(models.ProductCategory,pcid=id)
        myform=forms.ProductCategoryForm(request.POST,instance=obj);
        if myform.is_valid():
            myform.save();
        return redirect('showprocat')
    
class DeleteProCat(View):
    def get(self,request,id):
        obj=get_object_or_404(models.ProductCategory,pcid=id)
        return render(request,'delprocat.html',{'pcname':obj.pcname})
    def post(self,request,id):
        obj=get_object_or_404(models.ProductCategory,pcid=id);
        obj.delete();
        return redirect('showprocat')
    
class ProductView(View):
    def get(self,request):
        myform=forms.ProductForm();
        return render(request,'addpro.html',{'myform':myform})
    def post(self,request):
        myform=forms.ProductForm(request.POST)
        if myform.is_valid():
            myform.save();
        return redirect('home')
    
def showPro(request):
    data=models.Product.objects.all();
    return render(request,'showpro.html',{'mydata':data})

class UpdateProduct(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Product,pid=id)
        myform=forms.ProductForm(instance=obj)
        return render(request,'updpro.html',{'myform':myform})
    def post(self,request,id):
        obj=get_object_or_404(models.Product,pid=id)
        myform=forms.ProductForm(request.POST,instance=obj);
        if myform.is_valid():
            myform.save();
        return redirect('showpro')

class DeleteProduct(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Product,pid=id)
        return render(request,'delpro.html',{'pname':obj.pname})
    def post(self,request,id):
        obj=get_object_or_404(models.Product,pid=id);
        obj.delete();
        return redirect('showpro')
    
class ComplaintView(View):
    def get(self,request):
        myform=forms.ComplaintForm();
        return render(request,'addcomp.html',{'myform':myform})
    def post(self,request):
        try:
            cid=models.Complaints.objects.order_by('-compid')[0].compid;
            print("CID is : ",cid)
        except:
            cid=0;
        myform=forms.ComplaintForm(request.POST)
        # if myform.is_valid():
        print("Hello!!!!!!!")
        compdesc=request.POST['compdesc']
        compdt=datetime.today().date();
        status="open";
        userid= request.session['userid'];
        response=" ";
        # print(cid,compdesc,compdt,status,response,userid)
        ob=models.Complaints(cid+1,compdesc,compdt,status,response,userid)
        ob.save();
        return redirect('home')
        
def showComplaints(request):
    data=models.Complaints.objects.all();
    return render(request,'showcomp.html',{'mydata':data})

class Response(View):
    def get(self,request,id):
        obj=get_object_or_404(models.Complaints,compid=id)
        myform=forms.ComplaintForm(instance=obj);
        return render(request,'response.html',{'myform':myform})
    def post(self,requst,id):
        obj=get_object_or_404(models.Complaints,compid=id)
        myform=forms.ComplaintForm(requst.POST,instance=obj);
        if myform.is_valid():
            # res=requst.POST['response']
            myform.save();
            return redirect('showcomp')
        
class ShopView(View):
    prolist=[]
    def get(self,request):
        pcdata=models.ProductCategory.objects.all();
        return render(request,'shop.html',{'mydata':pcdata})
    def post(self,request):
        pid=request.POST['proid'];
        self.prolist.append(pid)
        request.session['mycart']=self.prolist;
        return redirect("home")      
    
def showProlist(request):
    pcdata=models.ProductCategory.objects.get(pcid=request.GET['id'])
    products=models.Product.objects.filter(pcid=pcdata.pcid)
    mydata=[]
    for pro in products:
        mydata.append(pro.get_pro())
    data=json.dumps(mydata)  #it is same as JSON.stringify()
    return HttpResponse(data)


class ShowCart(View):
    def get(self,request):
        cart=request.session['mycart']
        mydata=[]
        for i in cart:
            prodata=models.Product.objects.get(pid__exact=i)
            mydata.append(prodata)
        return render(request,'showcart.html',{'mydata':mydata})
    def post(self,request):
        uid=request.session['userid']
        userid1=models.UserMaster.objects.get(userid__exact=uid)
        proids=request.POST.getlist('chk')
        for i in proids:
            prodata=models.Product.objects.get(pid=i)
            obj=models.Orders(proid=prodata,userid=userid1)
            obj.save();
            request.session['mycart'].remove(i)
            request.session.modified=True;
        return redirect('cart')
        
    
def delcart(request,id):
    request.session['mycart'].remove(id);
    request.session.modified=True;
    return redirect('cart')


class ViewOrder(View):
    def get(self,request):
        uid=request.session['userid']
        userid1=models.UserMaster.objects.get(userid__exact=uid)
        mydata=models.Orders.objects.filter(userid=userid1)
        print(mydata)
        price=[]
        for items in mydata:
            total=items.proid.price-(items.proid.price*items.proid.discount)/100
            price.append(total);
        netprice=sum(price)
        return render(request,'showorder.html',{'mydata':mydata,'netprice':netprice})
    def post(self,request):
        return HttpResponse("<h1>Payment APIs is yet to Integrate</h1><hr>");