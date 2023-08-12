from django.db import models
import datetime


class UserMaster(models.Model):
    userid=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=10)
    def __str__(self):
        return self.usertype+"-"+self.userid;

class UserProfile(models.Model):
    username=models.CharField(max_length=30,primary_key=True)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    mob=models.CharField(max_length=10)
    email=models.EmailField()
    userid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class ProductCategory(models.Model):
    pcid=models.CharField(max_length=30,primary_key=True)
    pcname=models.CharField(max_length=30)
    def __str__(self):
        return self.pcid+"-"+self.pcname;
    
class Product(models.Model):
    pid=models.CharField(max_length=30,primary_key=True)
    pname=models.CharField(max_length=30)
    pdesc=models.CharField(max_length=100)
    price=models.IntegerField()
    discount=models.IntegerField()
    pcid=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.pid+"-"+self.pname;
    def get_pro(self):
        return {
            'pid':self.pid,
            'pname':self.pname,
            'pdesc':self.pdesc,
            'price':self.price,
            'discount':self.discount,
        }
        
        

    
class OrderMaster(models.Model):
    orderid=models.IntegerField(auto_created=True,primary_key=True)
    orderdate=models.DateField()
    amount=models.IntegerField()
    userid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)

class OrderDetails(models.Model):
    pid=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    netprice=models.IntegerField()
    orderid=models.IntegerField(auto_created=True,primary_key=True)

class Complaints(models.Model):
    compid=models.IntegerField(auto_created=True,primary_key=True)
    compdesc=models.CharField(max_length=500,null=True)
    compdt=models.DateField(null=True)
    status=models.CharField(max_length=30, default="open")
    response=models.CharField(max_length=400,default="Response Awaited",null=True)
    userid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.compid)+"-"+self.compdesc+"-"+self.status
    
class Orders(models.Model):
    proid=models.ForeignKey(Product,on_delete=models.CASCADE)
    orddt=models.DateField(default=datetime.date.today)
    userid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)

    