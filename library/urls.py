from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userAuth', views.userAuth, name='userAuth'),
    path('signIn',views.signIn,name='signIn'),
    path('signUp',views.signUp,name='signUp'),
    path('booksInfo',views.booksInfo,name='booksInfo'),
    path('returnablebooks',views.returnablebooks,name='returnablebooks'),
    path('borrowablebooks', views.borrowablebooks,name='borrowablebooks'),
    path('adminlogin', views.adminlogin,name='adminlogin'),
    path('admindashboard',views.admindashboard,name="admindashboard"),
    path('adminaddstudent', views.adminaddstudent,name='adminaddstudent'),
    path('adminaddbook', views.adminaddbook,name='adminaddbook')

]