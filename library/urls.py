from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userAuth', views.userAuth, name='userAuth'),
    path('signIn',views.signIn,name='signIn'),
    path('signUp',views.signUp,name='signUp'),
    path('booksInfo',views.bookInfo,name='booksInfo'),
    path('returnableBooks',views.returnableBooks,name='returnablebooks'),
    path('borrowableBooks', views.borrowableBooks,name='borrowablebooks')

]