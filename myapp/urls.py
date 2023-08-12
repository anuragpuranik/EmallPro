from django.urls import path
from . import views
urlpatterns = [
    #urls for Home page
    path('',views.home,name='home'),
    
    #urls for User Management
    path('adduser',views.AddUserView.as_view(),name='adduser'),
    path('logins',views.LoginView.as_view(),name='logins'),
    path('logouts',views.logouts,name='logouts'),
    path('profile',views.ProfileView.as_view(),name='profile'),
    path('showuser',views.ShowUsers.as_view(),name='showuser'),
    path('userdetails/<id>',views.UserDetailsView.as_view(),name='userdetails'),
    
    #urls for Product Categories
    path('addprocat',views.ProductCatView.as_view(),name='addprocat'),
    path('showprocat',views.showProCat,name='showprocat'),
    path('updprocat/<id>',views.UpdateProCat.as_view(),name='updprocat'),
    path('delprocat/<id>',views.DeleteProCat.as_view(),name='delprocat'),
      
    #urls for Product Management
    path('addpro',views.ProductView.as_view(),name='addpro'),
    path('showpro',views.showPro,name='showpro'),
    path('updpro/<id>',views.UpdateProduct.as_view(),name='updpro'),
    path('delpro/<id>',views.DeleteProduct.as_view(),name='delpro'),
    
    #urls for Complaints
    path('addcomp',views.ComplaintView.as_view(),name='addcomp'),
    path('showcomp',views.showComplaints,name='showcomp'),
    path('response/<id>',views.Response.as_view(),name='response'),
    
    
    #urls for Shopping
    path('shop',views.ShopView.as_view(),name='shop'),
    path('prolist',views.showProlist,name='prolist'),
    path('cart',views.ShowCart.as_view(),name='cart'),
    path('delcart/<id>',views.delcart,name='delcart'),
    path('showorder',views.ViewOrder.as_view(),name='showorder'),
]
