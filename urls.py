from django.urls import path
from .import views

urlpatterns = [
    path('',views.homee,name='homee'),
	path('accounts/login/',views.loginview,name="login"),
	path('logout',views.logout_view),
    path('accounts/sign_up/',views.sign_up,name="signup") ,
	path('reset',views.Resethome,name='reset'), 
	path('passwordreset',views.resetPassword,name='resetpassword'),
    path('home',views.home,name='home'), 
    path('add',views.add,name='add'), 
    path('addexp',views.addexp,name='addexp'), 
    path('update',views.update,name='update'), 
    path('updateb',views.updateb,name='updateb'), 
    path('viewex',views.viewex,name='viewex'), 
    path('delete',views.delete,name='delete'), 
    path('deleteexp',views.deleteexp,name='deleteexp'), 




]